BINARY_NAME=raidix

build:
        gcc -g -o ${BINARY_NAME} main.c

install:
        mkdir -p $(DESTDIR)/usr/bin
        install -m 0755 ${BINARY_NAME} $(DESTDIR)/usr/bin/${BINARY_NAME}

clean:
        rm ${BINARY_NAME}
