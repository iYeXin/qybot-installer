// 屏蔽F5刷新、Ctrl+R、Ctrl+F5
document.addEventListener('keydown', function (e) {
    // 屏蔽F5
    if (e.key === 'F5' || e.keyCode === 116) {
        e.preventDefault();
        e.returnValue = false;
    }

    // 屏蔽Ctrl+R
    if ((e.ctrlKey && e.key === 'r') || (e.ctrlKey && e.keyCode === 82)) {
        e.preventDefault();
        e.returnValue = false;
    }

    // 屏蔽Ctrl+F5（强制刷新）
    if (e.key === 'F5' && e.ctrlKey) {
        e.preventDefault();
        e.returnValue = false;
    }

    // 屏蔽F12开发者工具
    if (e.key === 'F12' || e.keyCode === 123) {
        e.preventDefault();
        e.returnValue = false;
    }
});

// 屏蔽右键菜单
document.addEventListener('contextmenu', function (e) {
    e.preventDefault();
    e.returnValue = false;
});

// 屏蔽Ctrl+Shift+I（开发者工具）
document.addEventListener('keydown', function (e) {
    if (e.ctrlKey && e.shiftKey && (e.key === 'I' || e.keyCode === 73)) {
        e.preventDefault();
        e.returnValue = false;
    }
});

// 屏蔽Ctrl+U（查看源代码）
document.addEventListener('keydown', function (e) {
    if (e.ctrlKey && (e.key === 'u' || e.keyCode === 85)) {
        e.preventDefault();
        e.returnValue = false;
    }
});

// 屏蔽Ctrl+S（保存网页）
document.addEventListener('keydown', function (e) {
    if (e.ctrlKey && (e.key === 's' || e.keyCode === 83)) {
        e.preventDefault();
        e.returnValue = false;
    }
});