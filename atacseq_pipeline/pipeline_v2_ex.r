# for any two filenames containing paired-end reads

chmod +x ./ATAC_67V_reseq1_1.fq.gz
chmod +x ./ATAC_67V_reseq1_2.fq.gz

# make a directory for all output files somehow?

#!/appl/fastqc-0.11.7/fastqc
fastqc ./ATAC_67V_reseq1_1.fq.gz
fastqc ./ATAC_67V_reseq1_2.fq.gz

#!/appl/jre-1.8.0_71/bin/java
# assumes that TruSeq3-PE.fa file exists in same directory
java -jar /appl/Trimmomatic-0.36/trimmomatic-0.36.jar PE ATAC_67V_reseq1_1.fq.gz ATAC_67V_reseq1_2.fq.gz out_67V_1P.fq.gz out_67V_1U.fq.gz out_67V_2P.fq.gz out_67V_2U.fq.gz ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36

chmod +x ./out_67V_1P.fq.gz
chmod +x ./out_67V_2P.fq.gz

#!/appl/bwa-0.7.17/bwa
# assumes that hg19 index files exist already
bwa aln ./bwa_index/hg19.fa ./out_67V_1P.fq.gz > 67V_1P.sai
bwa aln ./bwa_index/hg19.fa ./out_67V_2P.fq.gz > 67V_2P.sai

chmod +x 67V_1P.sai
chmod +x 67V_2P.sai

bwa sampe ./bwa_index/hg19.fa ./67V_1P.sai ./67V_2P.sai ./out_67V_1P.fq.gz ./out_67V_2P.fq.gz > aln.sam

chmod +x aln.sam