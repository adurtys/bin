#!/usr/bin/env python

# make a list of the filenames
filenames = ["ATAC_67S_reseq1_1.fq.gz", "ATAC_HMTB067S_1.fq.gz", "ATAC_67S_reseq1_2.fq.gz", 
"ATAC_HMTB067S_2.fq.gz", "ATAC_67V_reseq1_1.fq.gz", "ATAC_HMTB067V_1.fq.gz", "ATAC_67V_reseq1_2.fq.gz", 
"ATAC_HMTB067V_2.fq.gz"]

# for name in filenames:
    # run R commands within python ????
	
	# perform quality control analysis
	
	# perform adapter removal with trimmomatic

	# align reads to hg19 genome
	# STEP 1: generate alignments in suffix array coordinate
	# STEP 2: generate alignments in the SAM format
	# STEP 3: get multiple hits
	
	# sort mapped reads
	# perform quality control of alignment reads
	# remove mitochondrial reads
	# remove PCR duplicates
	# remove reads corresponding to overrepresented areas of the genome due to technical bias (?)
	# shift reads for Tn5 insertion (is this necessary?)

	# visualization
	# peak calling for regions of genomic enrichment
	# compare peaks with other peak files (BEDTools)
		# annotation of peaks
		# motif finding

# perform statistical analysis