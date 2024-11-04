# DOCKERFILE -- For common execution environment for DSA Project. INSTRUCTIONS:
# Run `docker build . -t plagiarism_checker` the first time to create the tagged image.
# Run `docker run --rm -it -v .:/plagiarism_checker plagiarism_checker`.
# This instanciates a container with the current directory mounted at /plagiarism_checker.
# NOTE: To use gdb and sanitizers properly, you should run it on native architecture.

FROM ubuntu:24.04

ENV TZ=Asia/Kolkata

RUN apt-get update && apt-get full-upgrade -y 

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install clang llvm libc++-dev libclang-dev lld gdb neovim git make sudo wget -y
RUN git clone https://github.com/VundleVim/Vundle.vim.git ~/.nvim/bundle/Vundle.vim
RUN mkdir ~/.config && mkdir ~/.config/nvim
RUN echo "source ~/.vimrc" > ~/.config/nvim/init.vim
RUN bash -c "$(wget https://gef.blah.cat/sh -O -)"

RUN printf "set number\nset expandtab\nset tabstop=4\nset shiftwidth=4\nset autoindent\nset smartindent\nset foldmethod=syntax\nautocmd Filetype c,cpp setlocal foldmethod=syntax\nautocmd Filetype make setlocal foldmethod=indent\nautocmd Filetype make setlocal noexpandtab\nlet g:python_highlight_all = 1\nset foldlevel=100\nset hls\nset nocompatible\nfiletype off\nset rtp+=~/.nvim/bundle/Vundle.vim\ncall vundle#begin()\nPlugin 'VundleVim/Vundle.vim'\nPlugin 'bfrg/vim-cpp-modern'\nPlugin 'scrooloose/nerdtree'\nPlugin 'itchyny/lightline.vim'\nPlugin 'jiangmiao/auto-pairs'\ncall vundle#end()\nfiletype plugin indent on\ncolorscheme desert\nsyntax on\nsyntax enable\nset backspace=indent,eol,start\nset laststatus=2\nset noshowmode\nset mouse=anv\n" > ~/.vimrc

RUN echo "PS1='\\[\\033[01;32m\\]\\u \\[\\033[01;35m\\]\\\\t \\[\\033[01;34m\\]\\W \\[\\033[01;32m\\]$\\[\\033[0m\\] '" >> ~/.bashrc
RUN echo "leak:llvm\nleak:_fetchInitializingClassList\nleak:__Balloc_D2A" >> /root/.lsan.supp

RUN printf "alias l='ls -A '\nalias ll='ls -AlSh '\nalias lr='ls -AlShR '\nalias rd='rm -rf '\nalias d='du -h -d 1 '\nalias sudo='sudo '\nalias cr='cp -rf '\nalias clear='reset && clear '\nexport CXX=clang++\nexport CC=clang\nexport CXXFLAGS='-std=c++20 -g -pthread -Wall -Wshadow -Wuninitialized -Wtype-limits'\nexport CFLAGS='-std=c17 -g -pthread -Wall -Wpedantic -Wshadow -Wuninitialized -Wtype-limits'\nexport LDFLAGS='-fuse-ld=lld'\nexport CSTRICT='-fsanitize=address,undefined,leak,bounds -Werror'\nexport CTHREAD='-fsanitize=thread,undefined,bounds -Werror'\nexport LSAN_OPTIONS=suppressions=/root/.lsan.supp\nalias h++='\$CXX \$CXXFLAGS -c '\nalias c++='\$CXX \$CXXFLAGS \$LDFLAGS '\nalias hpp='\$CXX \$CXXFLAGS -c '\nalias cpp='\$CXX \$CXXFLAGS \$LDFLAGS '\nalias hcc='\$CC \$CFLAGS -c '\nalias cc='\$CC \$CFLAGS \$LDFLAGS '\nalias h++strict='\$CXX \$CXXFLAGS \$CSTRICT -c '\nalias c++strict='\$CXX \$CXXFLAGS \$CSTRICT \$LDFLAGS '\nalias hppstrict='\$CXX \$CXXFLAGS \$CSTRICT -c '\nalias cppstrict='\$CXX \$CXXFLAGS \$CSTRICT \$LDFLAGS '\nalias hccstrict='\$CC \$CFLAGS \$CSTRICT -c '\nalias ccstrict='\$CC \$CFLAGS \$CSTRICT \$LDFLAGS '\nalias h++thread='\$CXX \$CXXFLAGS \$CTHREAD -c '\nalias c++thread='\$CXX \$CXXFLAGS \$CTHREAD \$LDFLAGS '\nalias hppthread='\$CXX \$CXXFLAGS \$CTHREAD -c '\nalias cppthread='\$CXX \$CXXFLAGS \$CTHREAD \$LDFLAGS '\nalias hccthread='\$CC \$CFLAGS \$CTHREAD -c '\nalias ccthread='\$CC \$CFLAGS \$CTHREAD \$LDFLAGS '\n" >> ~/.bashrc
RUN nvim +PluginInstall -c qall
RUN vim +PluginInstall -c qall

CMD ["/bin/bash"]
