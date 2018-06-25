#!/usr/bin/env python

# make a list of the filenames
filenames = ["ATAC_67S_reseq1_1.fq.gz", "ATAC_HMTB067S_1.fq.gz", "ATAC_67S_reseq1_2.fq.gz", 
"ATAC_HMTB067S_2.fq.gz", "ATAC_67V_reseq1_1.fq.gz", "ATAC_HMTB067V_1.fq.gz", "ATAC_67V_reseq1_2.fq.gz", 
"ATAC_HMTB067V_2.fq.gz"]

# for name in filenames:
        # run R commands within python ????
        # chmod +x filename
	
		# perform quality control analysis
		# fastqc ./filename
	
		# perform adaptor removal with trimmomatic
		# bsub -q voight_normal -o trimmomaticTest.out "java -jar /appl/Trimmomatic-0.36/trimmomatic-0.36.jar 
			# PE forward_file.fq.gz (ex: ATAC_67S_reseq1_1.fq.gz) reverse_file.fq.gz (ex: ATAC_67S_reseq1_2.fq.gz) 
			# forward_paired_out.fq.gz (ex: out_67S_1P.fq.gz) forward_unpaired_out.fq.gz (out_67S_1U.fq.gz) 
			# reverse_paired_out.fq.gz (ex: out_67S_2P.fq.gz) reverse_unpaired_out (ex: out_67S_2U.fq.gz) 
			# ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36"

		# align reads to hg19 genome
		# chmod +x forward_paired_out.fq.gz
		# chmod +x reverse_paired_out.fq.gz
		# STEP 1: generate alignments in suffix array coordinate
		# bsub -q voight_normal -o bwaTest1.out "bwa aln ../bwa_index/hg19.fa ./forward_paired_out.fq.gz 
			# (out_67S_1P.fq.gz) > filename1.sai (ex: 67S_1P.sai)"
		# bsub -q voight_normal -o bwaTest2.out "bwa aln ../bwa_index/hg19.fa ./reverse_paired_out.fq.gz 
			# (out_67S_2P.fq.gz) > filename2.sai (ex: 67S_2P.sai)"

		# STEP 2: generate alignments in the SAM format:
		# chmod +x filename1.sai
		# chmod +x filename2.sai
		# bsub -q voight_normal -o bwa_sam_align_test1.out "bwa sampe ../bwa_index/hg19.fa ./filename1.sai (ex: 67S_1P.sai)"
		# bsub -q voight_normal -o bwa_sam_align_test2.out "bwa sampe ../bwa_index/hg19.fa ./filename2.sai (ex: 67S_2P.sai)"

	# perform quality control of alignment reads
	# remove mitochondrial reads
	# remove PCR duplicates

	# peak calling for regions of genomic enrichment

	# visualization

	# compare peaks with other peak files (BEDTools)
		# annotation of peaks
		# motif finding
