# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.8

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\CMake\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\CMake\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\Dennis\workspace\iTrace\jni\TobiiTracker

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\Dennis\workspace\iTrace\jni\TobiiTracker\build

# Include any dependencies generated for this target.
include CMakeFiles/TobiiTracker.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/TobiiTracker.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/TobiiTracker.dir/flags.make

CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.obj: CMakeFiles/TobiiTracker.dir/flags.make
CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.obj: CMakeFiles/TobiiTracker.dir/includes_CXX.rsp
CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.obj: ../edu_ysu_itrace_trackers_TobiiTracker.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\Dennis\workspace\iTrace\jni\TobiiTracker\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.obj"
	C:\MinGW\bin\g++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\TobiiTracker.dir\edu_ysu_itrace_trackers_TobiiTracker.cpp.obj -c C:\Users\Dennis\workspace\iTrace\jni\TobiiTracker\edu_ysu_itrace_trackers_TobiiTracker.cpp

CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.i"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\Dennis\workspace\iTrace\jni\TobiiTracker\edu_ysu_itrace_trackers_TobiiTracker.cpp > CMakeFiles\TobiiTracker.dir\edu_ysu_itrace_trackers_TobiiTracker.cpp.i

CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.s"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\Dennis\workspace\iTrace\jni\TobiiTracker\edu_ysu_itrace_trackers_TobiiTracker.cpp -o CMakeFiles\TobiiTracker.dir\edu_ysu_itrace_trackers_TobiiTracker.cpp.s

CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.obj.requires:

.PHONY : CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.obj.requires

CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.obj.provides: CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.obj.requires
	$(MAKE) -f CMakeFiles\TobiiTracker.dir\build.make CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.obj.provides.build
.PHONY : CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.obj.provides

CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.obj.provides.build: CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.obj


# Object files for target TobiiTracker
TobiiTracker_OBJECTS = \
"CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.obj"

# External object files for target TobiiTracker
TobiiTracker_EXTERNAL_OBJECTS =

libTobiiTracker.dll: CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.obj
libTobiiTracker.dll: CMakeFiles/TobiiTracker.dir/build.make
libTobiiTracker.dll: C:/MinGW/lib/libboost_filesystem-mgw63-mt-1_64.a
libTobiiTracker.dll: C:/MinGW/lib/libboost_regex-mgw63-mt-1_64.a
libTobiiTracker.dll: C:/MinGW/lib/libboost_thread-mgw63-mt-1_64.a
libTobiiTracker.dll: C:/MinGW/lib/libboost_system-mgw63-mt-1_64.a
libTobiiTracker.dll: CMakeFiles/TobiiTracker.dir/linklibs.rsp
libTobiiTracker.dll: CMakeFiles/TobiiTracker.dir/objects1.rsp
libTobiiTracker.dll: CMakeFiles/TobiiTracker.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\Dennis\workspace\iTrace\jni\TobiiTracker\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libTobiiTracker.dll"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\TobiiTracker.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/TobiiTracker.dir/build: libTobiiTracker.dll

.PHONY : CMakeFiles/TobiiTracker.dir/build

CMakeFiles/TobiiTracker.dir/requires: CMakeFiles/TobiiTracker.dir/edu_ysu_itrace_trackers_TobiiTracker.cpp.obj.requires

.PHONY : CMakeFiles/TobiiTracker.dir/requires

CMakeFiles/TobiiTracker.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\TobiiTracker.dir\cmake_clean.cmake
.PHONY : CMakeFiles/TobiiTracker.dir/clean

CMakeFiles/TobiiTracker.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\Dennis\workspace\iTrace\jni\TobiiTracker C:\Users\Dennis\workspace\iTrace\jni\TobiiTracker C:\Users\Dennis\workspace\iTrace\jni\TobiiTracker\build C:\Users\Dennis\workspace\iTrace\jni\TobiiTracker\build C:\Users\Dennis\workspace\iTrace\jni\TobiiTracker\build\CMakeFiles\TobiiTracker.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/TobiiTracker.dir/depend

