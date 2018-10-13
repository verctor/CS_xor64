cld	
call	label1
label1:
jmp	label2
label5:
pop	{reg1}
mov	{reg2_32}, [{reg1}]
add	{reg1_32}, 4
mov	{reg4_32}, [{reg1}]
xor	{reg4_32}, {reg2_32}
add	{reg1_32}, 4
push	{reg1}
label4:
mov	{reg3_32}, [{reg1}]
xor	{reg3_32}, {reg2_32}
mov	[{reg1}], {reg3_32}
xor	{reg2_32}, {reg3_32}
add	{reg1_32}, 4
sub	{reg4_32}, 4
xor	{reg3_32}, {reg3_32}
cmp	{reg4_32}, {reg3_32}
je	label3
jmp	label4
label3:
pop	{reg2}
sub rsp, 8
jmp	{reg2}
label2:
call	label5
