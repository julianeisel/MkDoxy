from doxygen_snippets.doxygen import *
from doxygen_snippets.parser import *
from doxygen_snippets.generator import *

from beeprint import pp as pprint

if __name__ == '__main__':
	doxygenSource = "cpp_basic/src/"
	doxygenDest = "cpp_basic/doc/"
	doxygen = DoxygenRun(doxygenSource, doxygenDest)
	doxygen.run(print_command=True)

	doxyParsers = DoxygenParser(doxygenDest)
	parsedIndex = doxyParsers.getParsedIndex()
	# pprint(parsedIndex)

	parsedClass = doxyParsers.parseClass("Car")
	if not parsedClass:
		print("Class name error")
	# else:
		# pp(parsedClass)


	classCar = GenerateClassMd(parsedClass, "Car", "setWheelCount")
	# brief = classCar.getBrief()
	# detail = classCar.getDetail()
	# pp(classCar.generate())
	# pp(classCar.getFunction("setWheelCount"))
	pp(classCar.generate())

	# pprint(brief.getroottree())
	# pprint(classCar.generate())
	# pprint(detail)

	# pprint(brief)
