console.log('Hello World!')
async function testExec() {

    const resp = await Niva.api.process.currentDir()
    console.log(resp)

}
testExec()
let installOption = {
    chrome: false,
    appId: '',
    appSecret: ''
}

let desktopPath
(async function initDesktopPath() {
    desktopPath = (await Niva.api.os.dirs()).desktop
}())

let appDom = document.querySelector('#app')

function openPage(url) {
    Niva.api.process.open(url)
}

let nextPage = (function () {
    let count = 0
    return function () {
        appDom.innerHTML = htmls[count].html;
        if (count == htmls.length - 1) {
            startInstall()
        }
        if (count == 4) {
            pathOnload()
        }
        if (htmls[count].script) {
            const script = document.createElement('script');
            script.textContent = htmls[count].script;
            setTimeout(() => { document.body.appendChild(script); }, 100);
        }
        count++
    }
}())

function exitApp() {
    Niva.api.process.exit()
}

async function openFile(path) {
    const result = Niva.process.open(path)
}

async function pushMessage(level, title, message) {
    const data = await Niva.api.dialog.showMessage(title, message, level)
    return data
}

nextPage()

try {
    // downloadBinary('https://docs.qybot.yexin.wiki/assets/inter-roman-greek-ext.CqjqNYQ-.woff2').then(data => { console.log(data) })
    // Niva.api.http.get('https://docs.qybot.yexin.wiki/assets/inter-roman-greek-ext.CqjqNYQ-.woff2').then(data => {
    //     console.log(data)
    // })
    // fetch("https://docs.qybot.yexin.wiki/assets/inter-roman-greek-ext.CqjqNYQ-.woff2")
    //     .then((response) => response.json())
    //     .then((data) => console.log(data));
} catch (error) {

}