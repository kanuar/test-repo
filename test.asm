test_segment:
    la x3,test
    la x4,arr2
    li x5,0
    test_loop:
        lw x6,0(x3)
        lw x7,0(x4)
        beq x6,x0,final
        beq x7,x0,final
        slt x5,x6,x7
        bne x5,x0,final
        slt x5,x7,x6
        bne x5,x0,final
        addi x3,x3,4
        addi x4,x4,4
        j test_loop
final:
    mv a7,x5
