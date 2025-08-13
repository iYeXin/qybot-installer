function license2page() {
    const agree = document.querySelector('#agreeCheckbox');
    if (agree.checked) {
        nextPage()
    } else {
        pushMessage('info', 'QYbot 安装程序', '请阅读并同意《QYbot 使用声明》')
    }
}

function dependencies2page() {
    const chrome = document.querySelector('#installChrome');
    if (chrome.checked) installOption.chrome = true
    nextPage()
}

function credentials2page() {
    const appId = document.querySelector('#appId');
    const appSecret = document.querySelector('#appSecret');
    if (appId.value && appSecret.value) {
        installOption.appId = appId.value;
        installOption.appSecret = appSecret.value;
        nextPage()
    } else {
        pushMessage('info', 'QYbot 安装程序', '请输入有效的 AppId 和 AppSecret')
    }
}

let inputPath, installPath, shortcut

function pathOnload() {
    inputPath = document.querySelector('#installPath')
    inputPath.value = desktopPath
    installPath = desktopPath
    shortcut = document.querySelector('#createDesktopShortcut')
}

async function browseDirectory() {
    const data = await Niva.api.dialog.pickDir();
    if (data) {
        inputPath.value = data
        installPath = data
    }
}

function inputInstallPath(e) {
    if (e.target.value) {
        installPath = e.target.value
    }
}

async function directory2page() {
    let pathValid = await Niva.api.fs.exists(installPath)
    if ((installPath && pathValid) || installPath == 'C:\\Program Files\\QYbot\\v1.1.8') {
        installOption.shortcut = shortcut.checked
        installOption.path = installPath
        nextPage()
    } else {
        pushMessage('info', 'QYbot 安装程序', '请输入有效的安装路径')
    }
}