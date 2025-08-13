async function downloadBinary(url, options = {}) {
    const startTime = Date.now();

    const outputDir = options.outputDir || (await Niva.api.process.currentDir()) + "/__temp";
    const filename = options.filename || generateRandomFilename(url);
    const keepFile = options.keepFile ?? false;
    const returnBinary = options.returnBinary ?? true;
    const proxy = options.proxy; // 新增代理支持

    // 确保输出目录存在
    if (!(await Niva.api.fs.exists(outputDir))) {
        await Niva.api.fs.createDirAll(outputDir);
    }

    const outputPath = `${outputDir}/${filename}`;
    let binaryData = null;
    let size = 0;

    try {
        // 使用新的 HTTP 模块下载二进制数据
        const response = await Niva.api.http.fetch({
            url,
            responseType: "binary",
            proxy, // 支持代理
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status} ${response.statusText}`);
        }

        const base64Data = response.response.body;
        size = computeBase64Size(base64Data);

        // 需要保存文件或返回二进制数据时处理数据
        if (keepFile || returnBinary) {
            // 直接写入文件（如果需要保存）
            if (keepFile) {
                await Niva.api.fs.write(outputPath, base64Data, "base64");
            }

            // 转换为 Uint8Array（如果需要返回二进制）
            if (returnBinary) {
                binaryData = base64ToUint8Array(base64Data);
            }
        }

        return {
            outputPath: keepFile ? outputPath : undefined,
            binaryData,
            time: Date.now() - startTime,
            size
        };
    } catch (error) {
        // 错误处理：清理可能已创建的文件
        if (keepFile && await Niva.api.fs.exists(outputPath)) {
            try {
                await Niva.api.fs.remove(outputPath);
            } catch (cleanupError) {
                console.error("Cleanup failed:", cleanupError);
            }
        }

        const enhancedError = new Error(`Download failed: ${error.message}`);
        enhancedError.cause = error;
        throw enhancedError;
    }

    // 辅助函数：计算 Base64 数据大小
    function computeBase64Size(base64) {
        const padding = (base64.match(/=/g) || []).length;
        return (base64.length * 3) / 4 - padding;
    }

    // 辅助函数：生成随机文件名
    function generateRandomFilename(url) {
        const extMatch = url.match(/\.([a-z0-9]+)(?:[?#]|$)/i);
        const ext = extMatch ? extMatch[1] : "bin";
        return `file_${Date.now()}_${Math.random().toString(36).slice(2, 8)}.${ext}`;
    }

    // 辅助函数：Base64 转 Uint8Array
    function base64ToUint8Array(base64) {
        const binaryString = atob(base64);
        const len = binaryString.length;
        const bytes = new Uint8Array(len);
        for (let i = 0; i < len; i++) {
            bytes[i] = binaryString.charCodeAt(i);
        }
        return bytes;
    }
}
