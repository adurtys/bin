#!/usr/bin/env python

# make a list of the filenames
filenames = ["ATAC_67S_reseq1_1.fq.gz", "ATAC_HMTB067S_1.fq.gz", "ATAC_67S_reseq1_2.fq.gz", "ATAC_HMTB067S_2.fq.gz", "ATAC_67V_reseq1_1.fq.gz", "ATAC_HMTB067V_1.fq.gz", "ATAC_67V_reseq1_2.fq.gz", "ATAC_HMTB067V_2.fq.gz"]

# for name in filenames:
	# chmod +x filename
	
	# perform quality control analysis
	# fastqc ./filename
	
	# perform adaptor removal with trimmomatic
	# bsub -q voight_normal -o trimmomaticTest.out "java -jar /appl/Trimmomatic-0.36/trimmomatic-0.36.jar PE ATAC_67S_reseq1_1.fq.gz ATAC_67S_reseq1_2.fq.gz out_67S_1P.fq.gz out_67S_1U.fq.gz out_67S_2P.fq.gz out_67S_2U.fq.gz ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36"

	# align reads to hg19 genome

	# perform quality control of alignment reads
	# remove mitochondrial reads
	# remove PCR duplicates

	# peak calling for regions of genomic enrichment

	# visualization

	# compare peaks with other peak files (BEDTools)
		# annotation of peaks
		# motif finding
