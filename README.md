# Study Python 


## About Python 

### pip - Python package install

* install pip

        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        
        python get-pip.py

### Python的GIL

* CPython的线程是操作系统的原生线程。在Linux上为pthread，在Windows上为Win thread，完全由操作系统调度线程的执行。一个Python解释器进程内有一个主线程，以及多个用户程序的执行线程。即便使用多核心CPU平台，由于GIL的存在，也将禁止多线程的并行执行。[2]
* Python解释器进程内的多线程是以协作多任务方式执行。当一个线程遇到I/O任务时，将释放GIL。计算密集型（CPU-bound）的线程在执行大约100次解释器的计步（ticks）时，将释放GIL。计步（ticks）可粗略看作Python虚拟机的指令。计步实际上与时间片长度无关。可以通过sys.setcheckinterval()设置计步长度。
* 在单核CPU上，数百次的间隔检查才会导致一次线程切换。在多核CPU上，存在严重的线程颠簸（thrashing）。
* Python 3.2开始使用新的GIL。新的GIL实现中用一个固定的超时时间来指示当前的线程放弃全局锁。在当前线程保持这个锁，且其他线程请求这个锁时，当前线程就会在5毫秒后被强制释放该锁。
* 可以创建独立的进程来实现并行化。Python 2.6引进了多进程包multiprocessing。或者将关键组件用C/C++编写为Python扩展，通过ctypes使Python程序直接调用C语言编译的动态链接库的导出函数。