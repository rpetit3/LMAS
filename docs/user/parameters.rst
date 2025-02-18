Parameters
==========

A set of **default parameters** is provided, but these can be easily altered by either editing the 
``params.config`` file, or by passing the new value when executing the workflow with nextflow.
There are three main parameters in LMAS: **``--reference``, ``--fastq`` and ``--md``**. 

The **reference sequences**, in a single multifasta file, can be passed with the ``--reference`` parameter, and ``--fastq`` receives the 
**raw data** for assembly. The raw data is a collection of sequence fragments from the references and can be either 
obtained *in silico* or from real sequencing platforms. Users can pass text information, in a markdown file, 
on input samples to be presented in the report with the ``--md`` parameter.

Several options are available to alter the behaviour of the **assemblers** incorporated in LMAS, namely to alter 
the values of the k-mer for each assembly iteration. By default, these values reflect the corresponding default 
settings of the assemblers. 

The target values for some **quality assessment** metrics can also be adjusted, such as N50 and NG50.


Input Files
------------

fastq
^^^^^

Path expression to paired-end fastq files. Required.

* **Param:** :code:`--fastq`

* **Default:** :code:`data/fastq/*_{1,2}.*`


reference
^^^^^^^^^

Path to reference fasta file. Required.

* **Param:** :code:`--reference`

* **Default:** :code:`data/reference/*.fasta`


md
^^^

Path to markdown file with text to be displayed in the report. Optional.

* **Param:** :code:`--md`

* **Default:** :code:`data/*.md`


Assembler options
-----------------

BCALM2
^^^^^^
* **Param:** :code:`--bcalmKmerSize`

* **Definition:** K-mer size value

* **Default:** 31

GATB Minia Pipeline
^^^^^^^^^^^^^^^^^^^
* **Param:** :code:`--gatbkmer`

* **Definition:** String with list of k-mer sizes

* **Default:** '21,61,101,141,181'

------------

* **Param:** :code:`--gatb_besst_iter`

* **Definition:** Number of iteration during BESST scaffolding

* **Default:** 10000

------------

* **Param:** :code:`--GATB_error_correction`

* **Definition:** Boolean to perform error correction

* **Default:** false

Minia
^^^^^
* **Param:** :code:`--miniakmer`

* **Definition:** K-mer size value

* **Default:** 31

MEGAHIT
^^^^^^^
* **Param:** ``--megahitKmers``

* **Definition:** String with list of k-mer sizes

* **Default:** '21,29,39,59,79,99,119,141'

metaSPAdes
^^^^^^^^^^
* **Param:** :code:`--metaspadesKmers`

* **Definition:** String with the list of k-mer sizes or 'auto'

* **Default:** 'auto'

SPAdes
^^^^^^
* **Param:** :code:`--spadesKmers`

* **Definition:** String with the list of k-mer sizes or 'auto'

* **Default:** 'auto'

VelvetOptimizer
^^^^^^^^^^^^^^^
* **Param:** :code:`--velvetoptimizer_hashs`

* **Definition:** Start K-mer size value

* **Default:** 19

------------  

* **Param:** :code:`--velvetoptimizer_hashe`

* **Definition:** End K-mer size value

* **Default:** 31


Assembly Quality Assessment
---------------------------

Minimum contig length
^^^^^^^^^^^^^^^^^^^^^
Value for minimum contig length, in basepairs.

* **Param:** :code:`--minLength`

* **Default:** 1000

Mapped reads threshold
^^^^^^^^^^^^^^^^^^^^^^^
Value for the minimum percentage of a read length aligning to the contig to be considered as mapped.

* **Param:** :code:`--mapped_reads_threshold`

* **Default:** 0.75

N Target
^^^^^^^^
Target value for the N*x*, NA*x* and NG*x* metrics. 

* **Param:** :code:`--n_target`

* **Default:** 0.9

L Target
^^^^^^^^
Target value for the L*x* metric. 

* **Param:** :code:`--l_target`

* **Default:** 0.5
