function startInstall() {
    // 安装步骤顺序
    const steps = [
        { id: 'step-nodejs', name: 'Node.js', func: verifyNodeInstallation },
        { id: 'step-chrome', name: 'Chrome', func: installChromeIfNeeded },
        { id: 'step-directory', name: '创建目录', func: createInstallDirectory },
        { id: 'step-files', name: '复制文件', func: copyAndExtractFiles },
        { id: 'step-config', name: '写入配置', func: writeAppConfig },
        { id: 'step-shortcut', name: '快捷方式', func: createDesktopShortcut },
        // { id: 'step-launch', name: '启动应用', func: launchApplication }
    ];

    let currentStep = 0;
    const consoleOutput = document.getElementById('console-output');
    const finishButton = document.getElementById('finish-button');
    const alertBox = document.getElementById('install-alert');
    const alertMessage = document.getElementById('alert-message');
    const alertConfirm = document.getElementById('alert-confirm');
    const alertCancel = document.getElementById('alert-cancel');
    const progressFill = document.getElementById('progress-fill');
    const progressText = document.getElementById('progress-text');

    // 更新步骤状态
    function updateStepStatus(stepId, status, message) {
        const stepElement = document.getElementById(stepId);
        stepElement.classList.remove('running', 'success', 'error', 'skipped');
        stepElement.classList.add(status);

        const statusElement = stepElement.querySelector('.step-status');
        statusElement.textContent = message;
    }

    // 更新进度条
    function updateProgress(percent) {
        progressFill.style.width = percent + '%';
        progressText.textContent = Math.round(percent) + '%';
    }

    // 添加控制台输出
    function addConsoleMessage(message) {
        consoleOutput.textContent += '\n' + message;
        consoleOutput.scrollTop = consoleOutput.scrollHeight;
    }

    // 显示确认对话框
    function showAlert(message, callback) {
        alertMessage.textContent = message;
        alertBox.style.display = 'flex';

        alertConfirm.onclick = function () {
            alertBox.style.display = 'none';
            callback(true);
        };

        alertCancel.onclick = function () {
            alertBox.style.display = 'none';
            callback(false);
        };
    }

    // 执行安装过程
    async function runInstallation() {
        for (let i = 0; i < steps.length; i++) {
            currentStep = i;
            const step = steps[i];

            // 更新进度
            updateProgress((i / steps.length) * 100);

            // 更新UI为运行中状态
            updateStepStatus(step.id, 'running', '进行中...');
            addConsoleMessage('开始: ' + step.name);

            try {

                if (step.name === '复制文件') {
                    await new Promise(function (resolve) {
                        showAlert('将进行耗时操作，请耐心等待', function (confirmed) {
                            if (confirmed) {
                                addConsoleMessage('正在解压文件...');
                                resolve();
                            } else {
                                addConsoleMessage('用户取消');
                                throw new Error('安装被用户取消');
                            }
                        });
                    });
                }

                if (step.name === 'Node.js' || step.name === 'Chrome') {
                    await new Promise(function (resolve) {
                        showAlert(`如果您需要安装${step.name}，请在确认后耐心等待安装程序下载，并在弹出安装程序后手动进行安装操作`, function (confirmed) {
                            if (confirmed) {
                                addConsoleMessage('请等待下载...');
                                resolve();
                            } else {
                                addConsoleMessage('用户取消');
                                throw new Error('安装被用户取消');
                            }
                        });
                    });
                }

                if (step.name === '快捷方式') {
                    await new Promise(function (resolve) {
                        showAlert('请注意，安装程序将要静默创建快捷方式，部分安全软件可能拦截，请注意放行', function (confirmed) {
                            if (confirmed) {
                                addConsoleMessage('确认创建安装程序');
                                resolve();
                            } else {
                                addConsoleMessage('用户取消');
                                throw new Error('安装被用户取消');
                            }
                        });
                    });
                }

                // 执行安装函数
                const result = await step.func();

                // 更新状态
                if (result.status === 'success') {
                    updateStepStatus(step.id, 'success', result.message);
                    addConsoleMessage('✓ ' + result.message);
                } else if (result.status === 'skipped') {
                    updateStepStatus(step.id, 'skipped', result.message);
                    addConsoleMessage('↷ ' + result.message);
                } else if (result.status === 'pending') {
                    updateStepStatus(step.id, 'success', result.message);
                    addConsoleMessage('✓ ' + result.message);
                } else {
                    throw new Error(result.message);
                }
            } catch (error) {
                updateStepStatus(step.id, 'error', '失败');
                addConsoleMessage('✗ 错误: ' + error.message);
                addConsoleMessage('安装过程已中止');
                return;
            }

            // 更新进度
            updateProgress(((i + 1) / steps.length) * 100);
            await new Promise(resolve => setTimeout(resolve, 1000));
        }

        // 安装完成
        addConsoleMessage('✓ 安装完成！');
        finishButton.disabled = false;
        finishButton.textContent = '完成';
    }


    runInstallation();

    // 完成按钮事件
    finishButton.addEventListener('click', function () {
        // 关闭安装程序
        Niva.api.process.exit();
    });
}