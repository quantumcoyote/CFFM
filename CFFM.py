def loop():
    while True:
        id=1
        for x_1 in groups:
         for x_2 in groups:
          for x_3 in groups:
           for x_4 in groups:
            for x_5 in groups:
             for x_6 in groups:
              for x_7 in groups:
               for x_8 in groups:
                counter=0
                tmp=[]
                tmp.append(x_1)
                tmp.append(x_2)
                tmp.append(x_3)
                tmp.append(x_4)
                tmp.append(x_5)
                tmp.append(x_6)
                tmp.append(x_7)
                tmp.append(x_8)
                file_output=open('CFFM_'+str(id)+'.smi','w')
                for i in range(0, len(smiles)):
                 if i in positions:
                  file_output.write(str(tmp[counter]))
                  counter=counter+1
                 else:
                  file_output.write(str(smiles[i]))
                file_output.write('\n')
                id=id+1
                file_output.close()
        break

file_input = open('CFFM.smi','r')
smiles=file_input.readline()
file_input.close()
groups = ['','C(F)(F)C(F)(F)C(F)(F)C(F)(F)(F)','OC','Br']
positions=[]
for i in range(0,len(smiles)):
 if(smiles[i]=='X'):
     positions.append(i)

loop()
