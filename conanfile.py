from conans import ConanFile, CMake, tools


class TestlibrarypackConan(ConanFile):
    name = "TestLibraryPack"
    version = "1.0"
    license = "no license yet"
    author = "Farzeed farzeed.urrehman@foundry.com"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "Just a sample Testlibrarypack"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        #add in your git/perforce command to pull the source
        self.run("git clone https://github.com/FarzeedFoundry/Sample-Git.git")
        # https://github.com/FarzeedFoundry/Sample-Git.git

    def build(self):
        #git will make a sub folder so you need to account for it
        #print("")
        #self.run("cmake ../src/Sample-Git/")
        #self.run("make .")
        cmake = CMake(self)
        cmake.configure(source_dir = "./Sample-Git/")
        cmake.build()
 
 
    def package(self):
        #git will make a sub folder so you need to account for it with the headers unless you want the subfolder
        self.copy("*.h", dst="include", src=".")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.run("ls")
 
        self.copy(pattern="*Config.cmake", dst="cmake", keep_path=False) 
 
    def package_info(self):
        self.cpp_info.libs = ["TestLibrary"]
