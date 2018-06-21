#!/appl/R-3.2.5/bin/Rscript

# draw packages from Bioconductor
source("https://bioconductor.org/biocLite.R")
biocLite("GEOquery")
biocLite("oligo")
biocLite("limma")

# load packages into R
library(GEOquery)
library(oligo)
library(limma)

getGEOSuppFiles("GSE47516")