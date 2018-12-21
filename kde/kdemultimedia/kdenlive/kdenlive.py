import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()
        self.description = "Libre Video Editor, by KDE community"
        self.svnTargets['18.12'] = 'git://anongit.kde.org/kdenlive|Applications/18.12'
        self.svnTargets['19.04beta'] = 'git://anongit.kde.org/kdenlive|refactoring_timeline'
        self.defaultTarget = '18.12'

    def setDependencies(self):
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/qtdeclarative"] = None
        self.runtimeDependencies["libs/qt5/qtquickcontrols"] = None
        self.runtimeDependencies["libs/qt5/qtquickcontrols2"] = None
        self.runtimeDependencies["kde/frameworks/tier1/breeze-icons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/karchive"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kdbusaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kguiaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kitemviews"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kplotting"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kwidgetsaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier2/kcompletion"] = None
        self.runtimeDependencies["kde/frameworks/tier2/kcrash"] = None
        self.runtimeDependencies["kde/frameworks/tier2/kjobwidgets"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kdeclarative"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kbookmarks"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kconfigwidgets"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kiconthemes"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kio"] = None
        self.runtimeDependencies["kde/frameworks/tier3/knewstuff"] = None
        self.runtimeDependencies["kde/frameworks/tier3/knotifications"] = None
        self.runtimeDependencies["kde/frameworks/tier3/knotifyconfig"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kservice"] = None
        self.runtimeDependencies["kde/frameworks/tier3/ktextwidgets"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kxmlgui"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kinit"] = None
        self.runtimeDependencies["libs/ffmpeg"] = None
        self.runtimeDependencies["libs/mlt"] = None


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)

    def createPackage(self):
        self.blacklist_file.append(os.path.join(self.packageDir(), 'blacklist.txt'))
        self.ignoredPackages.append("libs/llvm-meta")
        self.ignoredPackages.append("data/hunspell-dictionaries")
        self.ignoredPackages.append("binary/mysql")

        self.defines["icon"] = os.path.join(self.buildDir(), "src", "kdenlive_SRCS.ico")
        self.defines["icon_png"] = os.path.join(self.sourceDir(), "kdenlive", "icons", "128-apps-kdenlive.png")
        self.defines["shortcuts"] = [{"name" : "Kdenlive", "target":"bin/kdenlive.exe", "description" : self.subinfo.description}]
        self.defines["mimetypes"] = ["application/x-kdenlive"]
        self.defines["file_types"] = [".kdenlive"]

        return TypePackager.createPackage(self)
