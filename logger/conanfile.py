from conans import ConanFile, CMake


class LoggerConan(ConanFile):
    name = "logger"
    version = "0.0"
    license = "public domain"
    author = "Rui Pires"
    url = "https://github.com/ruipires/conan-playground"
    description = "Just goofing around with logging"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "src/*"
    requires = "spdlog/1.3.1@bincrafters/stable"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["logger"]
