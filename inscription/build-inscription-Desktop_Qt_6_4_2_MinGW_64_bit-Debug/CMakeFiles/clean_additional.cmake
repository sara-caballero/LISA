# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\inscription_LISA_v2_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\inscription_LISA_v2_autogen.dir\\ParseCache.txt"
  "inscription_LISA_v2_autogen"
  )
endif()
