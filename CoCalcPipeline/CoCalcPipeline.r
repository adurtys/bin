#!/appl/R-3.2.5/bin/Rscript

# load libraries into R (assuming packages are already drawn from Bioconductor) 
library(GEOquery)
library(oligo)
library(limma)

# load file that maps phenotype to cel files
phenoData <- read.AnnotatedDataFrame("phenotype.csv", header = TRUE, sep = ",")
pData(phenoData)
