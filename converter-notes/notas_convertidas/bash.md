
--- 
title: "bash"
created: "2025-01-28T15:54:35,103613Z"
updated: "2025-09-17T11:58:07,889814Z"
tags: ['system:notebook:Kubernetes']
--- 

bash

#!/bin/bash
lista=tbEstabelecimento202409.csv

while read dados  
    do 
       arq=`echo $dados | awk -F"/" '{print$2}' |awk -F"." '{print$1}'`
       echo $dados | awk -F"," '{printf$2 $3 "\n" $4 $5 "\n"$6 $7 "\n"}' > $arq.pts
    done  < $lista

echo -e "\n\n\n Processo finalizado :) \n\n\n"

---x---

tar -cvf correcao-