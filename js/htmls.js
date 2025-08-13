let htmls = [
  {
    name: 'welcome',
    html: `<div class="installer welcome-container">
            <div class="welcome-hero">
                <img src="asset/hero.png" alt="QYbot Logo">
            </div>

            <div class="welcome-content">
                <h1 class="welcome-title">欢迎使用 QYbot 安装向导</h1>
                <p class="welcome-description">
                    轻量级、模块化的 QQ 机器人框架，快速构建智能聊天机器人
                </p>

                <ul class="welcome-features">
                    <li>插件化架构 - 轻松扩展机器人功能</li>
                    <li>图文混合回复 - 支持 Markdown 转图片</li>
                    <li>热重载机制 - 实时更新无需重启</li>
                    <li>官方插件市场 - 海量功能一键安装</li>
                </ul>

                <div class="welcome-actions">
                    <button class="installer-btn installer-btn-secondary" onclick="exitApp()">退出安装</button>
                    <button class="installer-btn installer-btn-primary" onclick="nextPage()">开始安装</button>
                </div>
            </div>
        </div>`
  },
  {
    name: 'license',
    html: `<div class="installer license-container">
            <div class="license-header">
                <h1 class="license-title">QYbot 使用声明</h1>
            </div>

            <div class="license-content">
                <h2>第一章 数据安全声明</h2>

                <h3>1.1 项目性质</h3>
                <p>QYbot 是一个开源的机器人框架：</p>
                <ul>
                    <li>项目源码托管于 GitHub：<span class="link" href="#" onclick="openPage('https://github.com/iYeXin/qybot/')">https://github.com/iYeXin/qybot/</span>
                    </li>
                    <li>遵循 MIT 开源许可证（<span class="link" href="#" onclick="openPage('https://github.com/iYeXin/qybot/blob/main/LICENSE')">查看许可证</span>）</li>
                    <li>接受社区代码审计与功能贡献</li>
                </ul>

                <h3>1.2 凭证隐私保护</h3>
                <p>用户输入的 QQ 开放平台 AppID 和 AppSecret 仅用于机器人身份验证：</p>
                <ul>
                    <li>凭证存储于用户本地设备</li>
                    <li>凭证仅用于与 QQ 平台进行通信</li>
                </ul>

                <h2>第二章 插件安全声明</h2>

                <h3>2.1 插件市场</h3>
                <p>插件市场平台仅提供分发服务，无法保证安全性</p>

                <h3>2.2 用户责任</h3>
                <p>使用插件时请注意：</p>
                <div class="license-warning">
                    <strong>! 警告</strong>
                    <ul>
                        <li>插件可能要求提供 API_KEY/账号密码等敏感信息</li>
                        <li>我们<strong>无法完全验证</strong>第三方插件的安全性</li>
                        <li>请自行评估插件来源可信度</li>
                    </ul>
                </div>

                <h2>第三章 免责条款</h2>

                <h3>3.1 责任范围界定</h3>
                <p>下列情况造成的损失概不承担责任：</p>
                <ul>
                    <li>因插件漏洞导致的数据泄露</li>
                    <li>未及时更新 IP 白名单造成的服务中断</li>
                    <li>使用非官方渠道获取的插件</li>
                    <li>未遵守 QQ 开放平台规则导致的封号</li>
                </ul>

                <h3>3.2 损失赔偿排除</h3>
                <p>我们不承担：</p>
                <ul>
                    <li>间接损失（利润损失/业务中断）</li>
                    <li>插件滥用导致的处罚金</li>
                    <li>用户凭证泄露引发的连带责任</li>
                </ul>

                <h2>第四章 协议生效</h2>

                <h3>4.1 生效方式</h3>
                <ul>
                    <li>您在通过官网进行资源下载和程序部署时需阅读本协议</li>
                    <li>Windows 安装包：勾选 "我已阅读并同意《QYbot 使用声明》" 后方可继续安装</li>
                </ul>
            </div>

            <div class="license-footer">
                <label class="license-agree">
                    <input type="checkbox" id="agreeCheckbox">
                    <span>我已阅读并同意《QYbot 使用声明》</span>
                </label>
                <div class="license-next">
                    <button class="installer-btn installer-btn-primary" id="nextButton" onclick="license2page()">下一步</button>
                </div>
            </div>
        </div>`
  },
  {
    name: "dependencies",
    html: `<div class="installer dependencies-container">
  <div class="dependencies-content">
    <div class="dependencies-icon">
      <svg viewBox="0 0 24 24">
        <path d="M21,16.5C21,16.88 20.79,17.21 20.47,17.38L12.57,21.82C12.41,21.94 12.21,22 12,22C11.79,22 11.59,21.94 11.43,21.82L3.53,17.38C3.21,17.21 3,16.88 3,16.5V7.5C3,7.12 3.21,6.79 3.53,6.62L11.43,2.18C11.59,2.06 11.79,2 12,2C12.21,2 12.41,2.06 12.57,2.18L20.47,6.62C20.79,6.79 21,7.12 21,7.5V16.5M12,4.15L5,8.09V15.91L12,19.85L19,15.91V8.09L12,4.15M12,12C12.55,12 13,12.45 13,13C13,13.55 12.55,14 12,14C11.45,14 11,13.55 11,13C11,12.45 11.45,12 12,12M12,15C12.55,15 13,15.45 13,16C13,16.55 12.55,17 12,17C11.45,17 11,16.55 11,16C11,15.45 11.45,15 12,15Z" />
      </svg>
    </div>
    
    <h2 class="dependencies-title">安装依赖环境</h2>
    
    <p class="dependencies-description">
      系统将自动检测并安装必要的运行环境：
      <br>
      <strong>Node.js</strong> - 核心运行环境（缺失将自动安装）
      <br>
      <strong>Chrome 浏览器</strong> - 图片生成功能所需（可选安装）
    </p>
    
    <div class="dependencies-option">
      <input type="checkbox" id="installChrome" checked>
      <label for="installChrome">
        同时安装 Chrome 浏览器（推荐）
        <br>
        <small style="color: #7F8C8D; font-weight: normal;">
          如设备已有 Chrome 或暂不需要图片生成功能，可取消勾选，你可以在安装 QYbot 后随时安装 Chrome 浏览器
        </small>
      </label>
    </div>

    <p class="dependencies-description">
        在安装过程中会同步进行依赖环境的安装，请注意在新窗口确认
    </p>
  </div>
  
  <div class="dependencies-footer">
    <button class="installer-btn installer-btn-primary" onclick="dependencies2page()">下一步</button>
  </div>
</div>
`
  },
  {
    name: "credentials",
    html: `<div class="installer credentials-container">
  <div class="credentials-content">
    <h2 class="credentials-title">配置机器人凭证</h2>
    
    <p class="credentials-description">
      请填写从 QQ 开放平台获取的 AppID 和 AppSecret：
      <br>
      进入<span class="link" href="#" onclick="openPage('https://q.qq.com/qqbot/#/developer/developer-setting')">开发管理页面</span>
      获取 <strong>AppId</strong> 和 <strong>AppSecret</strong>
      <br>
    </p>
    
    <div class="credentials-form">
      <div class="credentials-field">
        <label for="appId">AppID</label>
        <input type="text" id="appId" require placeholder="请输入您的 AppID">
      </div>
      
      <div class="credentials-field">
        <label for="appSecret">AppSecret</label>
        <input type="password" require id="appSecret" placeholder="请输入您的 AppSecret">
      </div>
      
    </div>
  </div>
  
  <div class="credentials-footer">
    <button class="installer-btn installer-btn-primary" onclick="credentials2page()">下一步</button>
  </div>
</div>
`
  },
  {
    name: "directory",
    html: `<div class="installer directory-container">
  <div class="directory-content">
    <h2 class="directory-title">选择安装位置</h2>
    
    <p class="directory-description">
      请选择 QYbot 的安装目录。
    </p>
    
    <div class="directory-form">
      <div class="directory-field">
        <label for="installPath">安装目录</label>
        <div class="directory-input-group">
          <input type="text" id="installPath" value="C:\\Program Files\\QYbot\\v1.1.8" oninput="inputInstallPath(event)">
          <button class="directory-browse-btn" onclick="browseDirectory()">浏览</button>
        </div>
      </div>
      
      <div class="directory-field">
        <label>
          <input type="checkbox" id="createDesktopShortcut" checked>
          创建桌面快捷方式
        </label>
      </div>

    </div>
  </div>
  
  <div class="directory-footer" onload="pathOnload()">
    <button class="installer-btn installer-btn-primary" onclick="directory2page()">下一步</button>
  </div>
</div>
`
  },
  {
    name: "startInstall",
    html: `<div class="installer installation-container">
  <div class="installation-header">
    <h2 class="installation-title">正在安装 QYbot</h2>
    <div class="installation-progress">
      <div class="progress-bar">
        <div class="progress-fill" id="progress-fill"></div>
      </div>
      <div class="progress-text" id="progress-text">0%</div>
    </div>
  </div>
  
  <div class="installation-steps">
    <div class="step-item" id="step-nodejs">
      <div class="step-icon"></div>
      <div class="step-info">
        <div class="step-name">Node.js</div>
        <div class="step-status">等待开始</div>
      </div>
    </div>
    
    <div class="step-item" id="step-chrome">
      <div class="step-icon"></div>
      <div class="step-info">
        <div class="step-name">Chrome</div>
        <div class="step-status">等待开始</div>
      </div>
    </div>
    
    <div class="step-item" id="step-directory">
      <div class="step-icon"></div>
      <div class="step-info">
        <div class="step-name">创建目录</div>
        <div class="step-status">等待开始</div>
      </div>
    </div>
    
    <div class="step-item" id="step-files">
      <div class="step-icon"></div>
      <div class="step-info">
        <div class="step-name">复制文件</div>
        <div class="step-status">等待开始</div>
      </div>
    </div>
    
    <div class="step-item" id="step-config">
      <div class="step-icon"></div>
      <div class="step-info">
        <div class="step-name">写入配置</div>
        <div class="step-status">等待开始</div>
      </div>
    </div>
    
    <div class="step-item" id="step-shortcut">
      <div class="step-icon"></div>
      <div class="step-info">
        <div class="step-name">快捷方式</div>
        <div class="step-status">等待开始</div>
      </div>
    </div>
  </div>
  
  <div class="installation-console">
    <pre id="console-output">准备开始安装...</pre>
  </div>
  
  <div class="installation-footer">
    <button class="installer-btn installer-btn-primary" id="finish-button" disabled>完成</button>
  </div>
  
  <div class="installation-alert" id="install-alert" style="display: none;">
    <div class="alert-content">
      <h3>安装提示</h3>
      <p id="alert-message"></p>
      <div class="alert-actions">
        <button class="installer-btn installer-btn-secondary" id="alert-cancel">取消</button>
        <button class="installer-btn installer-btn-primary" id="alert-confirm">继续</button>
      </div>
    </div>
  </div>
</div>


`
  }
]