def gen_interface(argc, argv):
    L=["typename T%d"%i for i in range(argc)]
    M=[]
    N=["t%d"%i for i in range(argc)]
    for i in range(argc):
        if (1 << i) & argv:
            M.append("const T%d& t%d"%(i,i))
        else:
            M.append("T%d& t%d"%(i,i))
    print "template <%s> inline TPIE_CLASS_NAME(%s) : factory(%s) {}"%(", ".join(L), ", ".join(M), ", ".join(N))
    

if __name__ == "__main__":
    print "// This file was generated by gen_pipe_constructors_inl.py, do not edit"
    print    

    print "inline TPIE_CLASS_NAME() : factory() {}"

    for i in range(1, 9):
        for j in range(2**i):
            gen_interface(i, j)
