// 步骤1: 验证Node.js安装
async function verifyNodeInstallation() {
    try {
        const { status, stdout } = await Niva.api.process.exec('node', ['-v'], { silent: true });
        if (status === 0 && stdout.trim().startsWith('v')) {
            return {
                status: 'success',
                message: `Node.js已安装 (${stdout.trim()})`
            };
        }
        throw new Error('Node.js未安装');
    } catch (error) {
        // 触发Node.js安装流程
        return installNode();
    }
}

// 步骤2: 安装Node.js
async function installNode() {
    try {
        const nodeUrl = 'https://qybot.yexin.wiki/download/node22/';
        const tempDir = (await Niva.api.os.dirs()).temp;
        const nodeInstaller = `${tempDir}\\node_installer.msi`;

        // 下载安装包
        const downloadResult = await downloadBinary(nodeUrl, {
            outputDir: tempDir,
            filename: 'node_installer.msi',
            keepFile: true
        });

        // 启动安装程序
        await Niva.api.process.open(downloadResult.outputPath);

        return {
            status: 'pending',
            message: 'Node.js安装程序已启动，请完成安装',
            data: { installerPath: downloadResult.outputPath }
        };
    } catch (error) {
        return {
            status: 'error',
            message: `Node安装失败: ${error.message}`
        };
    }
}

// 步骤3: 安装Chrome浏览器
async function installChromeIfNeeded() {
    if (!installOption.chrome) {
        return {
            status: 'skipped',
            message: '跳过Chrome安装'
        };
    }

    try {
        const chromeUrl = 'https://qybot.yexin.wiki/download/chrome/';
        const tempDir = (await Niva.api.os.dirs()).temp;
        const chromeInstaller = `${tempDir}\\chrome_installer.msi`;

        // 下载安装包
        const downloadResult = await downloadBinary(chromeUrl, {
            outputDir: tempDir,
            filename: 'chrome_installer.msi',
            keepFile: true
        });

        // 启动安装程序
        await Niva.api.process.open(downloadResult.outputPath);

        return {
            status: 'pending',
            message: 'Chrome安装程序已启动，请完成安装',
            data: { installerPath: downloadResult.outputPath }
        };
    } catch (error) {
        return {
            status: 'error',
            message: `Chrome安装失败: ${error.message}`
        };
    }
}

// 步骤4: 创建安装目录
async function createInstallDirectory() {
    try {
        const installPath = `${installOption.path}\\qybot`;

        // 创建父目录（如果不存在）
        const parentDir = installOption.path.substring(0, installOption.path.lastIndexOf('\\'));
        if (!(await Niva.api.fs.exists(parentDir))) {
            await Niva.api.fs.createDirAll(parentDir);
        }

        // 创建目标目录
        if (!(await Niva.api.fs.exists(installPath))) {
            await Niva.api.fs.createDir(installPath);
        }

        return {
            status: 'success',
            message: `安装目录已创建: ${installPath}`,
            data: { installPath }
        };
    } catch (error) {
        return {
            status: 'error',
            message: `目录创建失败: ${error.message}`
        };
    }
}

// 步骤5: 复制并解压应用文件
async function copyAndExtractFiles() {
    try {
        // const sourceFile = './qybot_v1.1.8.zip';
        const installPath = `${installOption.path}\\qybot`;
        const zipPath = `${installPath}\\qybot_v1.1.8.zip`;
        const exePath = `${installPath}\\qybot_v1.1.8.exe`;

        await Niva.api.fs.write(zipPath, zipBase64, 'base64')

        const unzip = await Niva.api.process.exec('powershell', [
            '-Command',
            `New-Item -ItemType Directory -Force -Path "${installPath}" | Out-Null; ` +
            `Expand-Archive -Path "${zipPath}" -DestinationPath "${installPath}" -Force`
        ], { silent: true });

        // 验证解压结果
        if (!(await Niva.api.fs.exists(exePath))) {
            throw new Error('主程序文件未找到');
        }

        return {
            status: 'success',
            message: '应用文件已复制并解压',
            data: { exePath }
        };
    } catch (error) {
        return {
            status: 'error',
            message: `文件处理失败: ${error.message}`
        };
    }
}

// 步骤6: 写入应用配置
async function writeAppConfig() {
    try {
        const configPath = `${installOption.path}\\qybot\\app.js`;
        const configTemplate = `
module.exports = {
    botConfig: {
        appId: '${installOption.appId}',
        secret: '${installOption.appSecret}',
        sandBox: true,
        imageServer: 'https://market.qybot.yexin.wiki/upload-image/',
    },
}`;

        // 写入配置文件
        await Niva.api.fs.write(configPath, configTemplate, 'utf8');

        return {
            status: 'success',
            message: '应用配置已更新'
        };
    } catch (error) {
        return {
            status: 'error',
            message: `配置写入失败: ${error.message}`
        };
    }
}

// 步骤7: 创建桌面快捷方式
async function createDesktopShortcut() {
    if (!installOption.shortcut) {
        return {
            status: 'skipped',
            message: '跳过快捷方式创建'
        };
    }

    try {
        const desktopPath = (await Niva.api.os.dirs()).desktop;
        if (!desktopPath) throw new Error('无法获取桌面路径');

        const exePath = `${installOption.path}\\qybot\\QYbot_v1.1.8.exe`;
        const shortcutPath = `${desktopPath}\\QYbot.lnk`;

        // 创建快捷方式
        const psCommand = [
            `$ws = New-Object -ComObject WScript.Shell`,
            `$sc = $ws.CreateShortcut("${shortcutPath}")`,
            `$sc.TargetPath = "${exePath}"`,
            `$sc.WorkingDirectory = "${installOption.path}\\qybot"`,
            `$sc.Save()`
        ].join('; ');

        const { status } = await Niva.api.process.exec(
            'powershell.exe',
            [
                '-NoProfile',          // 不加载用户配置文件
                '-ExecutionPolicy', 'Bypass', // 绕过执行策略
                '-WindowStyle', 'Hidden',    // 隐藏窗口
                '-NonInteractive',     // 非交互模式
                '-Command', psCommand
            ],
            { silent: true }
        );

        if (status !== 0) throw new Error('PowerShell命令执行失败');

        return {
            status: 'success',
            message: '桌面快捷方式已创建',
            data: { shortcutPath }
        };
    } catch (error) {
        return {
            status: 'error',
            message: `快捷方式创建失败: ${error.message}`
        };
    }
}

function blob2base64(blob) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result); // 转换完成后返回 Base64
        reader.onerror = () => reject(new Error("Blob 转换失败"));
        reader.readAsDataURL(blob); // 将 Blob 转换为 Base64
    });
}
