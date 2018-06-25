# example of steps in pipeline so far for one sample, 67S
# program currently runs in R environment from /project/voight_metprofiling/adurtys/atac_seq_pipeline

#!/appl/R-3.2.5/bin/Rscript

# make raw forward and reverse sequence reads executable
chmod +x ATAC_67S_reseq1_1.fq.gz ATAC_67S_reseq1_2.fq.gz

# perform fastQC analysis
bsub -q voight_normal -o 67S_fastQC_1.out "fastQC ./ATAC_67S_reseq1_1.fq.gz"
bsub -q voight_normal -o 67S_fastQC_2.out "fastQC ./ATAC_67S_reseq1_2.fq.gz"

# perform adapter removal
bsub -q voight_normal -o trimmomaticTest.out "java -jar /appl/Trimmomatic-0.36/trimmomatic-0.36.jar PE ATAC_67S_reseq1_1.fq.gz ATAC_67S_reseq1_2.fq.gz 
out_67S_1P.fq.gz out_67S_1U.fq.gz out_67S_2P.fq.gz out_67S_2U.fq.gz ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36"

# align reads to hg19 genome
chmod +x out_67S_1P.fq.gz out_67S_2P.fq.gz
bsub -q voight_normal -o bwaTest1.out "bwa aln ../bwa_index/hg19.fa ./out_67S_1P.fq.gz > 67S_1P.sai"
bsub -q voight_normal -o bwaTest2.out "bwa aln ../bwa_index/hg19.fa ./out_67S_2P.fq.gz > 67S_2P.sai"

chmod +x 67S_1P.sai 67S_2P.sai
bsub -q voight_normal -o bwa_sam_align_test.out "bwa sampe ../bwa_index/hg19.fa ./67S_1P.sai ./67S_2P.sai ./out_67S_1P.fq.gz ./out_67S_2P.fq.gz > aln.sam"
# OR:
# bsub -q voight_normal -o bwa_sam_align_test.out "bwa sampe ../bwa_index?hg19.fa ./67S_?.sai ./out_67S_?.fq.gz > aln.sam"

