from pwn import *
from struct import *
from itertools import permutations

context.arch = 'amd64'

def p32_b(u):
    return pack('>I', u)


x86_regs = [
    'eax', 'ebx', 'ecx', 'edx', 'esi', 'edi', 'ebp'
]
x64_regs = [
    'rax', 'rbx', 'rcx', 'rdx', 'rsi', 'rdi', 'rbp'
    #'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15'
]
template = open("xor64.S", 'r').read()

out = open('xor64.bin', 'wb')
for i in permutations(range(len(x64_regs)), 4):
    text = template.format(
        reg1=x64_regs[i[0]],
        reg2=x64_regs[i[1]],
        reg3=x64_regs[i[2]], 
        reg4=x64_regs[i[3]],
        reg1_32=x86_regs[i[0]],
        reg2_32=x86_regs[i[1]],
        reg3_32=x86_regs[i[2]],
        reg4_32=x86_regs[i[3]],
    )
    stub = asm(text)

    stub_len = p32_b(len(stub))
    out.write(stub_len + stub)

out.close()