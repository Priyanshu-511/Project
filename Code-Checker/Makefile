all: hi comp clean

hi:
	g++ -std=c++20 -o runn Timer.cpp main.cpp
	./runn

comp:
	g++ -std=c++20 -o work compare.cpp
	./work
	
clean:
	rm -rf run.txt
	rm -rf *.o
	rm -rf runn work

.PHONY: all hi comp clean
