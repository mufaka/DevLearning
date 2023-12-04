HEADERS = bmp.h helpers.h
OBJECTS = filter.o helpers.o

default: filter

%.o: %.c $(HEADERS)
	gcc -c $< -o $@

filter: $(OBJECTS)
	gcc $(OBJECTS) -o $@ -lm

clean:
	-rm -f $(OBJECTS)
	-rm -f filter