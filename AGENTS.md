# ImageTools — Agent 指南

## 快速开始

```powershell
pip install -r requirements.txt
python ImageTools.py          # 启动完整应用
python -m pytest              # 运行所有测试
python -m pytest test\components\test_basic_image.py  # 运行单个测试文件
```

## 架构

| 层 | 位置 | 用途 |
|---|------|------|
| 入口 | `ImageTools.py` | 创建 `QApplication`，打开 `MainWindow`，恢复上次会话 |
| 基础窗口 | `components/window.py` | `MainWindow`（应用外壳），`SubWindow`（所有工具的基类） |
| 工具实现 | `tools/*/` | 7 个工具：景深计算、抖动测试、图片编辑、RAW 图编辑、视频对比、PQtools 转代码、YUV 查看器 |
| 共享组件 | `components/` | `BasicImage.py`（核心图像操作）、`status_code_enum.py`（类型化错误）、`logconfig.py`、`property.py`（pickle 持久化） |
| UI（生成） | `components/ui/*.py`、`tools/*/*.py` | 从 `.ui` 文件通过 `pyside2-uic` / `pyside6-uic` 自动生成 |
| 资源（生成） | `resource_rc.py` | 从 `components/resource.qrc` 通过 `pyside2-rcc` 自动生成 |
| 独立构建 | `subapps/` | 薄启动器，通过 `sys.path.append("..")` 从 `tools/` 导入 |

**扩展新工具：**
1. 在 `tools/your_tool/` 下创建继承 `SubWindow` 的类
2. 在 `components/ui/mainwindow.ui` 中添加 `QAction`
3. 在 `ImageTools.subwindow_function` 中注册 action 到类的映射

## 关键约定

- **中文** 贯穿始终 — 注释、README、UI 字符串均为中文
- **`SubWindow` 基类** 通过 pickle 实现参数保存/恢复（关闭时写入 `config/<name>.tmp`）
- **状态持久化** 使用 `pickle` — 缓存位于 `config/`（已 gitignore）
- **日志** 写入 `log/YYYY-MM-DD.log`，启动时通过 `logconfig.clean_old_log()` 自动清理旧日志
- **自定义错误类型** 在 `components/status_code_enum.py` 中（`ImageToolError` 子类）
- **`QApplication.setStyle('Fusion')`** 在 `ImageTools.py` 和所有 `subapps/*.py` 中都有设置

## 构建与打包

```powershell
.\buildexe.bat                          # pyinstaller + Inno Setup
pyinstaller -w .\ImageTools.py --noconfirm  # 独立 exe
```

批处理脚本会清理 `build/` 和 `dist/`，安装 pyinstaller，然后运行它。构建后，`ImageTools.iss` 通过 Inno Setup（`compil32`）将结果打包成安装程序。

## 测试

- **框架：** pytest（`.vscode/settings.json`：`pytestEnabled: true`）
- **测试位置：** `test/components/`
- **资源：** `test/resource/`（jpg、png 文件）
- **无 `conftest.py` 或 `pytest.ini`** — 使用 pytest 默认配置
- 测试为功能/集成级别（加载文件、验证像素值、测试图像导航）

## 提交代码

- **整个用户请求完成后一次性提交**。开发过程中不因中间步骤反复提交（收集信息、小修小补都在本地积累，一次完整验证后统一提交）。
- 若用户请求明确分阶段，按阶段提交（如"先实现 X，再优化 Y"视为两个请求）。
- 基于 diff 中的事实，修改所有相关的文档，只更新与本次变更直接相关的段落，保持原有文档结构。
- 全部测试通过后自动提交本次变更，commit 信息采用中文结构化描述。
- 推送远端用 `git push origin HEAD:master`，需要用户显式确认。

## 注意事项

- `resource_rc.py` 是生成的 — **不要手动编辑**。通过 `pyside2-rcc -o resource_rc.py components/resource.qrc` 重新生成
- `.ui` 文件是源文件；对应的 `.py` 文件是生成的。编辑 `.ui`，然后重新生成
- `.vscode/settings.json` 中的 `pylintArgs` 白名单了 `PySide2,cv2`（旧的——当前依赖使用 `PySide6`；lint 报错时更新）
- `.gitignore` 排除了 `*.jpg`、`*.mp4`、`*.raw`、`config/` — 不要将测试夹具或本地状态提交到那里
- `subapps/*` 的独立启动器需要 `sys.path.append("..")` 才能找到 `tools/` 包
