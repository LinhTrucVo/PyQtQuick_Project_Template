## Getting Started

### Clone the Repository

To clone this repository with all submodules:

```bash
git clone --recurse-submodules https://github.com/LinhTrucVo/PyQtQuick_Project_Template.git
cd PyQtQuick_Project_Template
```

If you already cloned the repository without submodules, initialize them:

```bash
git submodule update --init --recursive
```

or update them:

```bash
git submodule update --remote --recursive
```

After update submodule:

```bash
git add src/PyQtLib_Project_Template
git commit -m "updare submodule"
git push
```

## Submodules

This project uses the following submodules:

- **PyQtLib_Project_Template**: Core PyQt threading and messaging library
  - Repository: https://github.com/LinhTrucVo/PyQtLib_Project_Template.git
  - Path: `src/PyQtLib_Project_Template`

# OLD-------------------------------------------------------------

# 🚀 QtQuick Project Template

[![Documentation Status](https://readthedocs.org/projects/pyqtquick-project-template/badge/?version=latest)](https://pyqtquick-project-template.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern template for PyQtQuick/PySide6 projects with multi-threaded QML UI integration.

---

## 📚 Official Documentation

👉 [https://pyqtquick-project-template.readthedocs.io/](https://pyqtquick-project-template.readthedocs.io/)

---

## 🎨 QML Preview Tools

- [QmlSandbox - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=SavenkovIgor.QmlSandboxExtension)
  <img src="https://img.icons8.com/color/48/000000/visual-studio-code-2019.png" width="24" alt="VSCode Icon"/>
- [Online preview of Qt Framework](https://try.qt.io/)
- [qmlonline](https://patrickelectric.work/qmlonline/)
- [QML Online (VSCode Extension)](https://marketplace.visualstudio.com/items?itemName=SavenkovIgor.QmlSandboxExtension)

---

## 🛠️ Features

- PySide6/PyQtQuick project structure
- Multi-threaded QML UI integration
- Sphinx documentation with PlantUML support
- Ready for Read the Docs

---

## 📦 Quick Start

```sh
git clone https://github.com/LinhTrucVo/PyQtQuick_Project_Template.git
cd PyQtQuick_Project_Template
# python -m venv .venv
# .venv\Scripts\activate  # On Windows
conda create --name PyQtQuick_Project_Template_env python=3.11 -y
conda activate PyQtQuick_Project_Template_env
pip install -r venv_requirements.txt
build.bat

```

## Create Code

```sh
cd src/lib/PyQtLib_Project_Template/tool
python create_client_code.py
```
<img width="267" height="182" alt="image" src="https://github.com/user-attachments/assets/885496ec-484c-4872-a762-7ae00c5685a8" />
