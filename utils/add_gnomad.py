from utils.vds_schema_string_utils import convert_vds_schema_string_to_annotate_variants_expr


GNOMAD_VDS_PATHS = {
    "exomes_37": "gs://gnomad-public/release/2.0.1/vds/exomes/gnomad.exomes.r2.0.1.sites.vds",
    "exomes_38": "gs://seqr-reference-data/GRCh38/gnomad/gnomad.exomes.r2.0.1.sites.liftover.b38.vds",
    "genomes_37": "gs://gnomad-public/release/2.0.1/vds/genomes/gnomad.genomes.r2.0.1.sites.vds",
    "genomes_38": "gs://seqr-reference-data/GRCh38/gnomad/gnomad.genomes.r2.0.1.sites.autosomes_and_X.liftover.b38.vds",
}


TOP_LEVEL_FIELDS = """
    rsid: String,
    qual: Double,
    filters: Set[String],
    pass: Boolean,
"""

INFO_FIELDS = """
    AC: Array[Int],
    AF: Array[Double],
    AN: Int,
    BaseQRankSum: Double,
    ClippingRankSum: Double,
    DB: Boolean,
    DP: Int,
    FS: Double,
    InbreedingCoeff: Double,
    MQ: Double,
    MQRankSum: Double,
    QD: Double,
    ReadPosRankSum: Double,
    SOR: Double,
    VQSLOD: Double,
    VQSR_culprit: String,
    VQSR_NEGATIVE_TRAIN_SITE: Boolean,
    VQSR_POSITIVE_TRAIN_SITE: Boolean,
    GQ_HIST_ALT: Array[String],
    DP_HIST_ALT: Array[String],
    AB_HIST_ALT: Array[String],
    GQ_HIST_ALL: String,
    DP_HIST_ALL: String,
    AB_HIST_ALL: String,
    AC_AFR: Array[Int],
    AC_AMR: Array[Int],
    AC_ASJ: Array[Int],
    AC_EAS: Array[Int],
    AC_FIN: Array[Int],
    AC_NFE: Array[Int],
    AC_OTH: Array[Int],
    AC_SAS: Array[Int],
    AC_Male: Array[Int],
    AC_Female: Array[Int],
    AN_AFR: Int,
    AN_AMR: Int,
    AN_ASJ: Int,
    AN_EAS: Int,
    AN_FIN: Int,
    AN_NFE: Int,
    AN_OTH: Int,
    AN_SAS: Int,
    AN_Male: Int,
    AN_Female: Int,
    AF_AFR: Array[Double],
    AF_AMR: Array[Double],
    AF_ASJ: Array[Double],
    AF_EAS: Array[Double],
    AF_FIN: Array[Double],
    AF_NFE: Array[Double],
    AF_OTH: Array[Double],
    AF_SAS: Array[Double],
    AF_Male: Array[Double],
    AF_Female: Array[Double],
    GC_AFR: Array[Int],
    GC_AMR: Array[Int],
    GC_ASJ: Array[Int],
    GC_EAS: Array[Int],
    GC_FIN: Array[Int],
    GC_NFE: Array[Int],
    GC_OTH: Array[Int],
    GC_SAS: Array[Int],
    GC_Male: Array[Int],
    GC_Female: Array[Int],
    AC_raw: Array[Int],
    AN_raw: Int,
    AF_raw: Array[Double],
    GC_raw: Array[Int],
    GC: Array[Int],
    Hom_AFR: Array[Int],
    Hom_AMR: Array[Int],
    Hom_ASJ: Array[Int],
    Hom_EAS: Array[Int],
    Hom_FIN: Array[Int],
    Hom_NFE: Array[Int],
    Hom_OTH: Array[Int],
    Hom_SAS: Array[Int],
    Hom_Male: Array[Int],
    Hom_Female: Array[Int],
    Hom_raw: Array[Int],
    Hom: Array[Int],
    STAR_AC: Int,
    STAR_AC_raw: Int,
    STAR_Hom: Int,
    POPMAX: Array[String],
    AC_POPMAX: Array[Int],
    AN_POPMAX: Array[Int],
    AF_POPMAX: Array[Double],
    DP_MEDIAN: Array[Int],
    DREF_MEDIAN: Array[Double],
    GQ_MEDIAN: Array[Int],
    AB_MEDIAN: Array[Double],
    AS_RF: Array[Double],
    AS_FilterStatus: Array[Set[String]],
    AS_RF_POSITIVE_TRAIN: Array[Int],
    AS_RF_NEGATIVE_TRAIN: Array[Int],
    CSQ: Array[String],
    AN_FIN_Male: Int,
    AN_EAS_Female: Int,
    AN_NFE_Female: Int,
    AC_AFR_Male: Array[Int],
    AN_AMR_Female: Int,
    AF_AMR_Male: Array[Double],
    Hemi_NFE: Array[Int],
    Hemi_AFR: Array[Int],
    AC_ASJ_Female: Array[Int],
    AF_FIN_Female: Array[Double],
    AN_ASJ_Male: Int,
    AC_OTH_Female: Array[Int],
    GC_OTH_Male: Array[Int],
    GC_FIN_Male: Array[Int],
    AC_NFE_Female: Array[Int],
    AC_EAS_Male: Array[Int],
    AC_OTH_Male: Array[Int],
    GC_SAS_Male: Array[Int],
    Hemi_AMR: Array[Int],
    AC_NFE_Male: Array[Int],
    Hemi: Array[Int],
    AN_FIN_Female: Int,
    GC_EAS_Male: Array[Int],
    GC_ASJ_Female: Array[Int],
    GC_SAS_Female: Array[Int],
    GC_ASJ_Male: Array[Int],
    Hemi_SAS: Array[Int],
    AN_ASJ_Female: Int,
    AF_FIN_Male: Array[Double],
    AN_OTH_Male: Int,
    AF_AFR_Male: Array[Double],
    STAR_Hemi: Int,
    AF_SAS_Male: Array[Double],
    Hemi_ASJ: Array[Int],
    AN_SAS_Female: Int,
    AN_AFR_Female: Int,
    Hemi_raw: Array[Int],
    AF_OTH_Male: Array[Double],
    AC_SAS_Female: Array[Int],
    AF_NFE_Female: Array[Double],
    AF_EAS_Female: Array[Double],
    AN_OTH_Female: Int,
    AF_EAS_Male: Array[Double],
    AF_SAS_Female: Array[Double],
    GC_AFR_Female: Array[Int],
    AF_AFR_Female: Array[Double],
    AC_FIN_Female: Array[Int],
    Hemi_OTH: Array[Int],
    GC_AMR_Male: Array[Int],
    AC_AFR_Female: Array[Int],
    GC_NFE_Male: Array[Int],
    AF_AMR_Female: Array[Double],
    GC_NFE_Female: Array[Int],
    AN_AFR_Male: Int,
    AN_NFE_Male: Int,
    AC_AMR_Male: Array[Int],
    GC_AMR_Female: Array[Int],
    AC_SAS_Male: Array[Int],
    AF_ASJ_Male: Array[Double],
    GC_FIN_Female: Array[Int],
    AC_EAS_Female: Array[Int],
    AC_AMR_Female: Array[Int],
    Hemi_FIN: Array[Int],
    AC_FIN_Male: Array[Int],
    GC_EAS_Female: Array[Int],
    AF_ASJ_Female: Array[Double],
    AF_OTH_Female: Array[Double],
    GC_AFR_Male: Array[Int],
    AN_SAS_Male: Int,
    AF_NFE_Male: Array[Double],
    AN_EAS_Male: Int,
    AC_ASJ_Male: Array[Int],
    Hemi_EAS: Array[Int],
    AN_AMR_Male: Int,
    GC_OTH_Female: Array[Int]
"""


def add_gnomad_to_vds(hail_context, vds, genome_version, exomes_or_genomes, root=None, top_level_fields=TOP_LEVEL_FIELDS, info_fields=INFO_FIELDS, verbose=True):
    if genome_version not in ("37", "38"):
        raise ValueError("Invalid genome_version: %s. Must be '37' or '38'" % str(genome_version))

    if exomes_or_genomes not in ("exomes", "genomes"):
        raise ValueError("Invalid genome_version: %s. Must be 'exomes' or 'genomes'" % str(genome_version))

    if root is None:
        root = "va.gnomad_%s" % exomes_or_genomes

    gnomad_vds_path = GNOMAD_VDS_PATHS["%s_%s" % (exomes_or_genomes, genome_version)]

    gnomad_vds = hail_context.read(gnomad_vds_path).split_multi()

    #if genome_version == "38":
        #info_fields += """
        #    OriginalContig: String,
        #    OriginalStart: String,
        #"""

    if exomes_or_genomes == "genomes":
        # remove any *SAS* fields from genomes since South Asian population only defined for exomes
        info_fields = "\n".join(field for field in info_fields.split("\n") if "SAS" not in field)

    top_fields_expr = convert_vds_schema_string_to_annotate_variants_expr(
        root=root,
        other_source_fields=top_level_fields,
        other_source_root="vds",
    )
    if verbose:
        print(top_fields_expr)

    info_fields_expr = convert_vds_schema_string_to_annotate_variants_expr(
        root=root,
        other_source_fields=info_fields,
        other_source_root="vds.info",
    )
    if verbose:
        print(info_fields_expr)

    return (vds
        .annotate_variants_vds(gnomad_vds, expr=top_fields_expr)
        .annotate_variants_vds(gnomad_vds, expr=info_fields_expr)
    )


"""
Struct{
    rsid: String,
    qual: Double,
    filters: Set[String],
    pass: Boolean,
    info: Struct{
        AC: Array[Int],
        AF: Array[Double],
        AN: Int,
        BaseQRankSum: Double,
        ClippingRankSum: Double,
        DB: Boolean,
        DP: Int,
        FS: Double,
        InbreedingCoeff: Double,
        MQ: Double,
        MQRankSum: Double,
        QD: Double,
        ReadPosRankSum: Double,
        SOR: Double,
        VQSLOD: Double,
        VQSR_culprit: String,
        VQSR_NEGATIVE_TRAIN_SITE: Boolean,
        VQSR_POSITIVE_TRAIN_SITE: Boolean,
        GQ_HIST_ALT: Array[String],
        DP_HIST_ALT: Array[String],
        AB_HIST_ALT: Array[String],
        GQ_HIST_ALL: String,
        DP_HIST_ALL: String,
        AB_HIST_ALL: String,
        AC_AFR: Array[Int],
        AC_AMR: Array[Int],
        AC_ASJ: Array[Int],
        AC_EAS: Array[Int],
        AC_FIN: Array[Int],
        AC_NFE: Array[Int],
        AC_OTH: Array[Int],
        AC_SAS: Array[Int],
        AC_Male: Array[Int],
        AC_Female: Array[Int],
        AN_AFR: Int,
        AN_AMR: Int,
        AN_ASJ: Int,
        AN_EAS: Int,
        AN_FIN: Int,
        AN_NFE: Int,
        AN_OTH: Int,
        AN_SAS: Int,
        AN_Male: Int,
        AN_Female: Int,
        AF_AFR: Array[Double],
        AF_AMR: Array[Double],
        AF_ASJ: Array[Double],
        AF_EAS: Array[Double],
        AF_FIN: Array[Double],
        AF_NFE: Array[Double],
        AF_OTH: Array[Double],
        AF_SAS: Array[Double],
        AF_Male: Array[Double],
        AF_Female: Array[Double],
        GC_AFR: Array[Int],
        GC_AMR: Array[Int],
        GC_ASJ: Array[Int],
        GC_EAS: Array[Int],
        GC_FIN: Array[Int],
        GC_NFE: Array[Int],
        GC_OTH: Array[Int],
        GC_SAS: Array[Int],
        GC_Male: Array[Int],
        GC_Female: Array[Int],
        AC_raw: Array[Int],
        AN_raw: Int,
        AF_raw: Array[Double],
        GC_raw: Array[Int],
        GC: Array[Int],
        Hom_AFR: Array[Int],
        Hom_AMR: Array[Int],
        Hom_ASJ: Array[Int],
        Hom_EAS: Array[Int],
        Hom_FIN: Array[Int],
        Hom_NFE: Array[Int],
        Hom_OTH: Array[Int],
        Hom_SAS: Array[Int],
        Hom_Male: Array[Int],
        Hom_Female: Array[Int],
        Hom_raw: Array[Int],
        Hom: Array[Int],
        STAR_AC: Int,
        STAR_AC_raw: Int,
        STAR_Hom: Int,
        POPMAX: Array[String],
        AC_POPMAX: Array[Int],
        AN_POPMAX: Array[Int],
        AF_POPMAX: Array[Double],
        DP_MEDIAN: Array[Int],
        DREF_MEDIAN: Array[Double],
        GQ_MEDIAN: Array[Int],
        AB_MEDIAN: Array[Double],
        AS_RF: Array[Double],
        AS_FilterStatus: Array[Set[String]],
        AS_RF_POSITIVE_TRAIN: Array[Int],
        AS_RF_NEGATIVE_TRAIN: Array[Int],
        CSQ: Array[String],
        AN_FIN_Male: Int,
        AN_EAS_Female: Int,
        AN_NFE_Female: Int,
        AC_AFR_Male: Array[Int],
        AN_AMR_Female: Int,
        AF_AMR_Male: Array[Double],
        Hemi_NFE: Array[Int],
        Hemi_AFR: Array[Int],
        AC_ASJ_Female: Array[Int],
        AF_FIN_Female: Array[Double],
        AN_ASJ_Male: Int,
        AC_OTH_Female: Array[Int],
        GC_OTH_Male: Array[Int],
        GC_FIN_Male: Array[Int],
        AC_NFE_Female: Array[Int],
        AC_EAS_Male: Array[Int],
        AC_OTH_Male: Array[Int],
        GC_SAS_Male: Array[Int],
        Hemi_AMR: Array[Int],
        AC_NFE_Male: Array[Int],
        Hemi: Array[Int],
        AN_FIN_Female: Int,
        GC_EAS_Male: Array[Int],
        GC_ASJ_Female: Array[Int],
        GC_SAS_Female: Array[Int],
        GC_ASJ_Male: Array[Int],
        Hemi_SAS: Array[Int],
        AN_ASJ_Female: Int,
        AF_FIN_Male: Array[Double],
        AN_OTH_Male: Int,
        AF_AFR_Male: Array[Double],
        STAR_Hemi: Int,
        AF_SAS_Male: Array[Double],
        Hemi_ASJ: Array[Int],
        AN_SAS_Female: Int,
        AN_AFR_Female: Int,
        Hemi_raw: Array[Int],
        AF_OTH_Male: Array[Double],
        AC_SAS_Female: Array[Int],
        AF_NFE_Female: Array[Double],
        AF_EAS_Female: Array[Double],
        AN_OTH_Female: Int,
        AF_EAS_Male: Array[Double],
        AF_SAS_Female: Array[Double],
        GC_AFR_Female: Array[Int],
        AF_AFR_Female: Array[Double],
        AC_FIN_Female: Array[Int],
        Hemi_OTH: Array[Int],
        GC_AMR_Male: Array[Int],
        AC_AFR_Female: Array[Int],
        GC_NFE_Male: Array[Int],
        AF_AMR_Female: Array[Double],
        GC_NFE_Female: Array[Int],
        AN_AFR_Male: Int,
        AN_NFE_Male: Int,
        AC_AMR_Male: Array[Int],
        GC_AMR_Female: Array[Int],
        AC_SAS_Male: Array[Int],
        AF_ASJ_Male: Array[Double],
        GC_FIN_Female: Array[Int],
        AC_EAS_Female: Array[Int],
        AC_AMR_Female: Array[Int],
        Hemi_FIN: Array[Int],
        AC_FIN_Male: Array[Int],
        GC_EAS_Female: Array[Int],
        AF_ASJ_Female: Array[Double],
        AF_OTH_Female: Array[Double],
        GC_AFR_Male: Array[Int],
        AN_SAS_Male: Int,
        AF_NFE_Male: Array[Double],
        AN_EAS_Male: Int,
        AC_ASJ_Male: Array[Int],
        Hemi_EAS: Array[Int],
        AN_AMR_Male: Int,
        GC_OTH_Female: Array[Int]
    },
    vep: Struct{
        assembly_name: String,
        allele_string: String,
        ancestral: String,
        colocated_variants: Array[Struct{
            aa_allele: String,
            aa_maf: Double,
            afr_allele: String,
            afr_maf: Double,
            allele_string: String,
            amr_allele: String,
            amr_maf: Double,
            clin_sig: Array[String],
            end: Int,
            eas_allele: String,
            eas_maf: Double,
            ea_allele: String,
            ea_maf: Double,
            eur_allele: String,
            eur_maf: Double,
            exac_adj_allele: String,
            exac_adj_maf: Double,
            exac_allele: String,
            exac_afr_allele: String,
            exac_afr_maf: Double,
            exac_amr_allele: String,
            exac_amr_maf: Double,
            exac_eas_allele: String,
            exac_eas_maf: Double,
            exac_fin_allele: String,
            exac_fin_maf: Double,
            exac_maf: Double,
            exac_nfe_allele: String,
            exac_nfe_maf: Double,
            exac_oth_allele: String,
            exac_oth_maf: Double,
            exac_sas_allele: String,
            exac_sas_maf: Double,
            id: String,
            minor_allele: String,
            minor_allele_freq: Double,
            phenotype_or_disease: Int,
            pubmed: Array[Int],
            sas_allele: String,
            sas_maf: Double,
            somatic: Int,
            start: Int,
            strand: Int
        }],
        context: String,
        end: Int,
        id: String,
        input: String,
        intergenic_consequences: Array[Struct{
            allele_num: Int,
            consequence_terms: Array[String],
            impact: String,
            minimised: Int,
            variant_allele: String
        }],
        most_severe_consequence: String,
        motif_feature_consequences: Array[Struct{
            allele_num: Int,
            consequence_terms: Array[String],
            high_inf_pos: String,
            impact: String,
            minimised: Int,
            motif_feature_id: String,
            motif_name: String,
            motif_pos: Int,
            motif_score_change: Double,
            strand: Int,
            variant_allele: String
        }],
        regulatory_feature_consequences: Array[Struct{
            allele_num: Int,
            biotype: String,
            consequence_terms: Array[String],
            impact: String,
            minimised: Int,
            regulatory_feature_id: String,
            variant_allele: String
        }],
        seq_region_name: String,
        start: Int,
        strand: Int,
        transcript_consequences: Array[Struct{
            allele_num: Int,
            amino_acids: String,
            biotype: String,
            canonical: Int,
            ccds: String,
            cdna_start: Int,
            cdna_end: Int,
            cds_end: Int,
            cds_start: Int,
            codons: String,
            consequence_terms: Array[String],
            distance: Int,
            domains: Array[Struct{
                db: String,
                name: String
            }],
            exon: String,
            gene_id: String,
            gene_pheno: Int,
            gene_symbol: String,
            gene_symbol_source: String,
            hgnc_id: Int,
            hgvsc: String,
            hgvsp: String,
            hgvs_offset: Int,
            impact: String,
            intron: String,
            lof: String,
            lof_flags: String,
            lof_filter: String,
            lof_info: String,
            minimised: Int,
            polyphen_prediction: String,
            polyphen_score: Double,
            protein_end: Int,
            protein_start: Int,
            protein_id: String,
            sift_prediction: String,
            sift_score: Double,
            strand: Int,
            swissprot: String,
            transcript_id: String,
            trembl: String,
            uniparc: String,
            variant_allele: String
        }],
        variant_class: String
    }
}
"""
