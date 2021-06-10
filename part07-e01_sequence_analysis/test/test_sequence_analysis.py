#!/usr/bin/env python3

import numpy as np

from collections import defaultdict, Counter
from itertools import product

import unittest
from unittest.mock import patch, MagicMock

from tmc import points
from tmc.utils import load, get_stdout, patch_helper
from numpy.testing import assert_allclose

import nbformat
import sys
import os

inputnb = "src/project_notebook_sequence_analysis.ipynb"

nb = nbformat.read(inputnb, as_version=4)

ol = __name__
__name__ = sys.argv[0]

for cell in nb.cells:
    if cell.cell_type == "code":
        exec(cell.source)

__name__ = ol

@points('p07-01.1')
class TestDnaToRna(unittest.TestCase):

    def test_dna_to_rna(self):
        self.assertEqual(dna_to_rna("ACGT"), "ACGU")
        self.assertNotEqual(dna_to_rna("ACGT"), "ACGT")

    def test_dna_to_rna_empty(self):
        self.assertEqual(dna_to_rna(""), "")


@points('p07-01.2')
class TestDict(unittest.TestCase):

    def test_size(self):
        d = get_dict()
        self.assertEqual(len(d), 64, msg="Incorrect number of elements in the returned dict!")

    def test_content(self):
        d = get_dict()

        self.assertIn("UUU", d, msg="The dict did not contain key UUU")
        self.assertEqual(d["UUU"], "F", msg="Incorrect amino acid for codon UUU")

        self.assertIn("UCU", d, msg="The dict did not contain key UCU")
        self.assertEqual(d["UCU"], "S", msg="Incorrect amino acid for codon UCU")

        self.assertIn("UAU", d, msg="The dict did not contain key UAU")
        self.assertEqual(d["UAU"], "Y", msg="Incorrect amino acid for codon UAU")

        self.assertIn("UGU", d, msg="The dict did not contain key UGU")
        self.assertEqual(d["UGU"], "C", msg="Incorrect amino acid for codon UGU")

        self.assertIn("UUC", d, msg="The dict did not contain key UUC")
        self.assertEqual(d["UUC"], "F", msg="Incorrect amino acid for codon UUC")

        self.assertIn("UCC", d, msg="The dict did not contain key UCC")
        self.assertEqual(d["UCC"], "S", msg="Incorrect amino acid for codon UCC")

        self.assertIn("UAC", d, msg="The dict did not contain key UAC")
        self.assertEqual(d["UAC"], "Y", msg="Incorrect amino acid for codon UAC")

        self.assertIn("UGC", d, msg="The dict did not contain key UGC")
        self.assertEqual(d["UGC"], "C", msg="Incorrect amino acid for codon UGC")

        self.assertIn("UUA", d, msg="The dict did not contain key UUA")
        self.assertEqual(d["UUA"], "L", msg="Incorrect amino acid for codon UUA")

        self.assertIn("UCA", d, msg="The dict did not contain key UCA")
        self.assertEqual(d["UCA"], "S", msg="Incorrect amino acid for codon UCA")

        self.assertIn("UAA", d, msg="The dict did not contain key UAA")
        self.assertEqual(d["UAA"], "*", msg="Incorrect amino acid for codon UAA")

        self.assertIn("UGA", d, msg="The dict did not contain key UGA")
        self.assertEqual(d["UGA"], "*", msg="Incorrect amino acid for codon UGA")

        self.assertIn("UUG", d, msg="The dict did not contain key UUG")
        self.assertEqual(d["UUG"], "L", msg="Incorrect amino acid for codon UUG")

        self.assertIn("UCG", d, msg="The dict did not contain key UCG")
        self.assertEqual(d["UCG"], "S", msg="Incorrect amino acid for codon UCG")

        self.assertIn("UAG", d, msg="The dict did not contain key UAG")
        self.assertEqual(d["UAG"], "*", msg="Incorrect amino acid for codon UAG")

        self.assertIn("UGG", d, msg="The dict did not contain key UGG")
        self.assertEqual(d["UGG"], "W", msg="Incorrect amino acid for codon UGG")

        self.assertIn("CUU", d, msg="The dict did not contain key CUU")
        self.assertEqual(d["CUU"], "L", msg="Incorrect amino acid for codon CUU")

        self.assertIn("CCU", d, msg="The dict did not contain key CCU")
        self.assertEqual(d["CCU"], "P", msg="Incorrect amino acid for codon CCU")

        self.assertIn("CAU", d, msg="The dict did not contain key CAU")
        self.assertEqual(d["CAU"], "H", msg="Incorrect amino acid for codon CAU")

        self.assertIn("CGU", d, msg="The dict did not contain key CGU")
        self.assertEqual(d["CGU"], "R", msg="Incorrect amino acid for codon CGU")

        self.assertIn("CUC", d, msg="The dict did not contain key CUC")
        self.assertEqual(d["CUC"], "L", msg="Incorrect amino acid for codon CUC")

        self.assertIn("CCC", d, msg="The dict did not contain key CCC")
        self.assertEqual(d["CCC"], "P", msg="Incorrect amino acid for codon CCC")

        self.assertIn("CAC", d, msg="The dict did not contain key CAC")
        self.assertEqual(d["CAC"], "H", msg="Incorrect amino acid for codon CAC")

        self.assertIn("CGC", d, msg="The dict did not contain key CGC")
        self.assertEqual(d["CGC"], "R", msg="Incorrect amino acid for codon CGC")

        self.assertIn("CUA", d, msg="The dict did not contain key CUA")
        self.assertEqual(d["CUA"], "L", msg="Incorrect amino acid for codon CUA")

        self.assertIn("CCA", d, msg="The dict did not contain key CCA")
        self.assertEqual(d["CCA"], "P", msg="Incorrect amino acid for codon CCA")

        self.assertIn("CAA", d, msg="The dict did not contain key CAA")
        self.assertEqual(d["CAA"], "Q", msg="Incorrect amino acid for codon CAA")

        self.assertIn("CGA", d, msg="The dict did not contain key CGA")
        self.assertEqual(d["CGA"], "R", msg="Incorrect amino acid for codon CGA")

        self.assertIn("CUG", d, msg="The dict did not contain key CUG")
        self.assertEqual(d["CUG"], "L", msg="Incorrect amino acid for codon CUG")

        self.assertIn("CCG", d, msg="The dict did not contain key CCG")
        self.assertEqual(d["CCG"], "P", msg="Incorrect amino acid for codon CCG")

        self.assertIn("CAG", d, msg="The dict did not contain key CAG")
        self.assertEqual(d["CAG"], "Q", msg="Incorrect amino acid for codon CAG")

        self.assertIn("CGG", d, msg="The dict did not contain key CGG")
        self.assertEqual(d["CGG"], "R", msg="Incorrect amino acid for codon CGG")

        self.assertIn("AUU", d, msg="The dict did not contain key AUU")
        self.assertEqual(d["AUU"], "I", msg="Incorrect amino acid for codon AUU")

        self.assertIn("ACU", d, msg="The dict did not contain key ACU")
        self.assertEqual(d["ACU"], "T", msg="Incorrect amino acid for codon ACU")

        self.assertIn("AAU", d, msg="The dict did not contain key AAU")
        self.assertEqual(d["AAU"], "N", msg="Incorrect amino acid for codon AAU")

        self.assertIn("AGU", d, msg="The dict did not contain key AGU")
        self.assertEqual(d["AGU"], "S", msg="Incorrect amino acid for codon AGU")

        self.assertIn("AUC", d, msg="The dict did not contain key AUC")
        self.assertEqual(d["AUC"], "I", msg="Incorrect amino acid for codon AUC")

        self.assertIn("ACC", d, msg="The dict did not contain key ACC")
        self.assertEqual(d["ACC"], "T", msg="Incorrect amino acid for codon ACC")

        self.assertIn("AAC", d, msg="The dict did not contain key AAC")
        self.assertEqual(d["AAC"], "N", msg="Incorrect amino acid for codon AAC")

        self.assertIn("AGC", d, msg="The dict did not contain key AGC")
        self.assertEqual(d["AGC"], "S", msg="Incorrect amino acid for codon AGC")

        self.assertIn("AUA", d, msg="The dict did not contain key AUA")
        self.assertEqual(d["AUA"], "I", msg="Incorrect amino acid for codon AUA")

        self.assertIn("ACA", d, msg="The dict did not contain key ACA")
        self.assertEqual(d["ACA"], "T", msg="Incorrect amino acid for codon ACA")

        self.assertIn("AAA", d, msg="The dict did not contain key AAA")
        self.assertEqual(d["AAA"], "K", msg="Incorrect amino acid for codon AAA")

        self.assertIn("AGA", d, msg="The dict did not contain key AGA")
        self.assertEqual(d["AGA"], "R", msg="Incorrect amino acid for codon AGA")

        self.assertIn("AUG", d, msg="The dict did not contain key AUG")
        self.assertEqual(d["AUG"], "M", msg="Incorrect amino acid for codon AUG")

        self.assertIn("ACG", d, msg="The dict did not contain key ACG")
        self.assertEqual(d["ACG"], "T", msg="Incorrect amino acid for codon ACG")

        self.assertIn("AAG", d, msg="The dict did not contain key AAG")
        self.assertEqual(d["AAG"], "K", msg="Incorrect amino acid for codon AAG")

        self.assertIn("AGG", d, msg="The dict did not contain key AGG")
        self.assertEqual(d["AGG"], "R", msg="Incorrect amino acid for codon AGG")

        self.assertIn("GUU", d, msg="The dict did not contain key GUU")
        self.assertEqual(d["GUU"], "V", msg="Incorrect amino acid for codon GUU")

        self.assertIn("GCU", d, msg="The dict did not contain key GCU")
        self.assertEqual(d["GCU"], "A", msg="Incorrect amino acid for codon GCU")

        self.assertIn("GAU", d, msg="The dict did not contain key GAU")
        self.assertEqual(d["GAU"], "D", msg="Incorrect amino acid for codon GAU")

        self.assertIn("GGU", d, msg="The dict did not contain key GGU")
        self.assertEqual(d["GGU"], "G", msg="Incorrect amino acid for codon GGU")

        self.assertIn("GUC", d, msg="The dict did not contain key GUC")
        self.assertEqual(d["GUC"], "V", msg="Incorrect amino acid for codon GUC")

        self.assertIn("GCC", d, msg="The dict did not contain key GCC")
        self.assertEqual(d["GCC"], "A", msg="Incorrect amino acid for codon GCC")

        self.assertIn("GAC", d, msg="The dict did not contain key GAC")
        self.assertEqual(d["GAC"], "D", msg="Incorrect amino acid for codon GAC")

        self.assertIn("GGC", d, msg="The dict did not contain key GGC")
        self.assertEqual(d["GGC"], "G", msg="Incorrect amino acid for codon GGC")

        self.assertIn("GUA", d, msg="The dict did not contain key GUA")
        self.assertEqual(d["GUA"], "V", msg="Incorrect amino acid for codon GUA")

        self.assertIn("GCA", d, msg="The dict did not contain key GCA")
        self.assertEqual(d["GCA"], "A", msg="Incorrect amino acid for codon GCA")

        self.assertIn("GAA", d, msg="The dict did not contain key GAA")
        self.assertEqual(d["GAA"], "E", msg="Incorrect amino acid for codon GAA")

        self.assertIn("GGA", d, msg="The dict did not contain key GGA")
        self.assertEqual(d["GGA"], "G", msg="Incorrect amino acid for codon GGA")

        self.assertIn("GUG", d, msg="The dict did not contain key GUG")
        self.assertEqual(d["GUG"], "V", msg="Incorrect amino acid for codon GUG")

        self.assertIn("GCG", d, msg="The dict did not contain key GCG")
        self.assertEqual(d["GCG"], "A", msg="Incorrect amino acid for codon GCG")

        self.assertIn("GAG", d, msg="The dict did not contain key GAG")
        self.assertEqual(d["GAG"], "E", msg="Incorrect amino acid for codon GAG")

        self.assertIn("GGG", d, msg="The dict did not contain key GGG")
        self.assertEqual(d["GGG"], "G", msg="Incorrect amino acid for codon GGG")


@points('p07-01.3')
class TestDictList(unittest.TestCase):

    def test_content(self):
        d = get_dict_list()
        self.assertIn("F", d, msg="amino acid F not found in dictionary!")
        self.assertEqual(set(d["F"]), set(['UUU', 'UUC']), msg="Invalid codons for amino acid F!")
        self.assertIn("S", d, msg="amino acid S not found in dictionary!")
        self.assertEqual(set(d["S"]), set(['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC']), msg="Invalid codons for amino acid S!")
        self.assertIn("Y", d, msg="amino acid Y not found in dictionary!")
        self.assertEqual(set(d["Y"]), set(['UAU', 'UAC']), msg="Invalid codons for amino acid Y!")
        self.assertIn("C", d, msg="amino acid C not found in dictionary!")
        self.assertEqual(set(d["C"]), set(['UGU', 'UGC']), msg="Invalid codons for amino acid C!")
        self.assertIn("L", d, msg="amino acid L not found in dictionary!")
        self.assertEqual(set(d["L"]), set(['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG']), msg="Invalid codons for amino acid L!")
        self.assertIn("*", d, msg="amino acid * not found in dictionary!")
        self.assertEqual(set(d["*"]), set(['UAA', 'UGA', 'UAG']), msg="Invalid codons for amino acid *!")
        self.assertIn("W", d, msg="amino acid W not found in dictionary!")
        self.assertEqual(set(d["W"]), set(['UGG']), msg="Invalid codons for amino acid W!")
        self.assertIn("P", d, msg="amino acid P not found in dictionary!")
        self.assertEqual(set(d["P"]), set(['CCU', 'CCC', 'CCA', 'CCG']), msg="Invalid codons for amino acid P!")
        self.assertIn("H", d, msg="amino acid H not found in dictionary!")
        self.assertEqual(set(d["H"]), set(['CAU', 'CAC']), msg="Invalid codons for amino acid H!")
        self.assertIn("R", d, msg="amino acid R not found in dictionary!")
        self.assertEqual(set(d["R"]), set(['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']), msg="Invalid codons for amino acid R!")
        self.assertIn("Q", d, msg="amino acid Q not found in dictionary!")
        self.assertEqual(set(d["Q"]), set(['CAA', 'CAG']), msg="Invalid codons for amino acid Q!")
        self.assertIn("I", d, msg="amino acid I not found in dictionary!")
        self.assertEqual(set(d["I"]), set(['AUU', 'AUC', 'AUA']), msg="Invalid codons for amino acid I!")
        self.assertIn("T", d, msg="amino acid T not found in dictionary!")
        self.assertEqual(set(d["T"]), set(['ACU', 'ACC', 'ACA', 'ACG']), msg="Invalid codons for amino acid T!")
        self.assertIn("N", d, msg="amino acid N not found in dictionary!")
        self.assertEqual(set(d["N"]), set(['AAU', 'AAC']), msg="Invalid codons for amino acid N!")
        self.assertIn("K", d, msg="amino acid K not found in dictionary!")
        self.assertEqual(set(d["K"]), set(['AAA', 'AAG']), msg="Invalid codons for amino acid K!")
        self.assertIn("M", d, msg="amino acid M not found in dictionary!")
        self.assertEqual(set(d["M"]), set(['AUG']), msg="Invalid codons for amino acid M!")
        self.assertIn("V", d, msg="amino acid V not found in dictionary!")
        self.assertEqual(set(d["V"]), set(['GUU', 'GUC', 'GUA', 'GUG']), msg="Invalid codons for amino acid V!")
        self.assertIn("A", d, msg="amino acid A not found in dictionary!")
        self.assertEqual(set(d["A"]), set(['GCU', 'GCC', 'GCA', 'GCG']), msg="Invalid codons for amino acid A!")
        self.assertIn("D", d, msg="amino acid D not found in dictionary!")
        self.assertEqual(set(d["D"]), set(['GAU', 'GAC']), msg="Invalid codons for amino acid D!")
        self.assertIn("G", d, msg="amino acid G not found in dictionary!")
        self.assertEqual(set(d["G"]), set(['GGU', 'GGC', 'GGA', 'GGG']), msg="Invalid codons for amino acid G!")
        self.assertIn("E", d, msg="amino acid E not found in dictionary!")
        self.assertEqual(set(d["E"]), set(['GAA', 'GAG']), msg="Invalid codons for amino acid E!")

    def test_size(self):
        d = get_dict_list()
        self.assertEqual(len(d), 21)


@points('p07-01.4')
class TestDnaToProt(unittest.TestCase):

    def test_first(self):
        self.assertEqual(dna_to_prot("ATGATATCATCGACGATGTAG"), "MISSTM*")

    def test_empty(self):
        self.assertEqual(dna_to_prot(""), "")


@points('p07-01.5')
class TestCodonToProb(unittest.TestCase):

    def test_size(self):
        d = get_probabability_dict()
        self.assertEqual(len(d), 64)

    def test_content(self):
        d = get_probabability_dict()
        self.assertIn("UUU", d, msg="Codon UUU was not found in the dictionary!")
        self.assertAlmostEqual(d["UUU"], 0.4641342698782968, places=4, msg="Incorrect probability of codon UUU!")
        self.assertIn("UCU", d, msg="Codon UCU was not found in the dictionary!")
        self.assertAlmostEqual(d["UCU"], 0.18758584014344437, places=4, msg="Incorrect probability of codon UCU!")
        self.assertIn("UAU", d, msg="Codon UAU was not found in the dictionary!")
        self.assertAlmostEqual(d["UAU"], 0.443338109266921, places=4, msg="Incorrect probability of codon UAU!")
        self.assertIn("UGU", d, msg="Codon UGU was not found in the dictionary!")
        self.assertAlmostEqual(d["UGU"], 0.45615733050366836, places=4, msg="Incorrect probability of codon UGU!")
        self.assertIn("UUC", d, msg="Codon UUC was not found in the dictionary!")
        self.assertAlmostEqual(d["UUC"], 0.5358657301217032, places=4, msg="Incorrect probability of codon UUC!")
        self.assertIn("UCC", d, msg="Codon UCC was not found in the dictionary!")
        self.assertAlmostEqual(d["UCC"], 0.21795953165920925, places=4, msg="Incorrect probability of codon UCC!")
        self.assertIn("UAC", d, msg="Codon UAC was not found in the dictionary!")
        self.assertAlmostEqual(d["UAC"], 0.5566618907330789, places=4, msg="Incorrect probability of codon UAC!")
        self.assertIn("UGC", d, msg="Codon UGC was not found in the dictionary!")
        self.assertAlmostEqual(d["UGC"], 0.5438426694963316, places=4, msg="Incorrect probability of codon UGC!")
        self.assertIn("UUA", d, msg="Codon UUA was not found in the dictionary!")
        self.assertAlmostEqual(d["UUA"], 0.07656764558436285, places=4, msg="Incorrect probability of codon UUA!")
        self.assertIn("UCA", d, msg="Codon UCA was not found in the dictionary!")
        self.assertAlmostEqual(d["UCA"], 0.15051714801827132, places=4, msg="Incorrect probability of codon UCA!")
        self.assertIn("UAA", d, msg="Codon UAA was not found in the dictionary!")
        self.assertAlmostEqual(d["UAA"], 0.29701911804823383, places=4, msg="Incorrect probability of codon UAA!")
        self.assertIn("UGA", d, msg="Codon UGA was not found in the dictionary!")
        self.assertAlmostEqual(d["UGA"], 0.46624296805302623, places=4, msg="Incorrect probability of codon UGA!")
        self.assertIn("UUG", d, msg="Codon UUG was not found in the dictionary!")
        self.assertAlmostEqual(d["UUG"], 0.1290578537068707, places=4, msg="Incorrect probability of codon UUG!")
        self.assertIn("UCG", d, msg="Codon UCG was not found in the dictionary!")
        self.assertAlmostEqual(d["UCG"], 0.05439771371883908, places=4, msg="Incorrect probability of codon UCG!")
        self.assertIn("UAG", d, msg="Codon UAG was not found in the dictionary!")
        self.assertAlmostEqual(d["UAG"], 0.23673791389873997, places=4, msg="Incorrect probability of codon UAG!")
        self.assertIn("UGG", d, msg="Codon UGG was not found in the dictionary!")
        self.assertAlmostEqual(d["UGG"], 1.0, places=4, msg="Incorrect probability of codon UGG!")
        self.assertIn("CUU", d, msg="Codon CUU was not found in the dictionary!")
        self.assertAlmostEqual(d["CUU"], 0.13171591206484023, places=4, msg="Incorrect probability of codon CUU!")
        self.assertIn("CCU", d, msg="Codon CCU was not found in the dictionary!")
        self.assertAlmostEqual(d["CCU"], 0.2867313296570278, places=4, msg="Incorrect probability of codon CCU!")
        self.assertIn("CAU", d, msg="Codon CAU was not found in the dictionary!")
        self.assertAlmostEqual(d["CAU"], 0.4185152128433691, places=4, msg="Incorrect probability of codon CAU!")
        self.assertIn("CGU", d, msg="Codon CGU was not found in the dictionary!")
        self.assertAlmostEqual(d["CGU"], 0.08010752804820104, places=4, msg="Incorrect probability of codon CGU!")
        self.assertIn("CUC", d, msg="Codon CUC was not found in the dictionary!")
        self.assertAlmostEqual(d["CUC"], 0.1955768259144855, places=4, msg="Incorrect probability of codon CUC!")
        self.assertIn("CCC", d, msg="Codon CCC was not found in the dictionary!")
        self.assertAlmostEqual(d["CCC"], 0.3234703981288551, places=4, msg="Incorrect probability of codon CCC!")
        self.assertIn("CAC", d, msg="Codon CAC was not found in the dictionary!")
        self.assertAlmostEqual(d["CAC"], 0.5814847871566309, places=4, msg="Incorrect probability of codon CAC!")
        self.assertIn("CGC", d, msg="Codon CGC was not found in the dictionary!")
        self.assertAlmostEqual(d["CGC"], 0.18377662978978224, places=4, msg="Incorrect probability of codon CGC!")
        self.assertIn("CUA", d, msg="Codon CUA was not found in the dictionary!")
        self.assertAlmostEqual(d["CUA"], 0.0713801723134756, places=4, msg="Incorrect probability of codon CUA!")
        self.assertIn("CCA", d, msg="Codon CCA was not found in the dictionary!")
        self.assertAlmostEqual(d["CCA"], 0.2766025276376192, places=4, msg="Incorrect probability of codon CCA!")
        self.assertIn("CAA", d, msg="Codon CAA was not found in the dictionary!")
        self.assertAlmostEqual(d["CAA"], 0.26501675921017337, places=4, msg="Incorrect probability of codon CAA!")
        self.assertIn("CGA", d, msg="Codon CGA was not found in the dictionary!")
        self.assertAlmostEqual(d["CGA"], 0.1088124833207855, places=4, msg="Incorrect probability of codon CGA!")
        self.assertIn("CUG", d, msg="Codon CUG was not found in the dictionary!")
        self.assertAlmostEqual(d["CUG"], 0.39570159041596514, places=4, msg="Incorrect probability of codon CUG!")
        self.assertIn("CCG", d, msg="Codon CCG was not found in the dictionary!")
        self.assertAlmostEqual(d["CCG"], 0.11319574457649788, places=4, msg="Incorrect probability of codon CCG!")
        self.assertIn("CAG", d, msg="Codon CAG was not found in the dictionary!")
        self.assertAlmostEqual(d["CAG"], 0.7349832407898266, places=4, msg="Incorrect probability of codon CAG!")
        self.assertIn("CGG", d, msg="Codon CGG was not found in the dictionary!")
        self.assertAlmostEqual(d["CGG"], 0.20155434006721587, places=4, msg="Incorrect probability of codon CGG!")
        self.assertIn("AUU", d, msg="Codon AUU was not found in the dictionary!")
        self.assertAlmostEqual(d["AUU"], 0.36107219301206106, places=4, msg="Incorrect probability of codon AUU!")
        self.assertIn("ACU", d, msg="Codon ACU was not found in the dictionary!")
        self.assertAlmostEqual(d["ACU"], 0.2467688440166039, places=4, msg="Incorrect probability of codon ACU!")
        self.assertIn("AAU", d, msg="Codon AAU was not found in the dictionary!")
        self.assertAlmostEqual(d["AAU"], 0.4703669907468028, places=4, msg="Incorrect probability of codon AAU!")
        self.assertIn("AGU", d, msg="Codon AGU was not found in the dictionary!")
        self.assertAlmostEqual(d["AGU"], 0.14960182300967595, places=4, msg="Incorrect probability of codon AGU!")
        self.assertIn("AUC", d, msg="Codon AUC was not found in the dictionary!")
        self.assertAlmostEqual(d["AUC"], 0.4698662895003286, places=4, msg="Incorrect probability of codon AUC!")
        self.assertIn("ACC", d, msg="Codon ACC was not found in the dictionary!")
        self.assertAlmostEqual(d["ACC"], 0.35523154074391966, places=4, msg="Incorrect probability of codon ACC!")
        self.assertIn("AAC", d, msg="Codon AAC was not found in the dictionary!")
        self.assertAlmostEqual(d["AAC"], 0.5296330092531971, places=4, msg="Incorrect probability of codon AAC!")
        self.assertIn("AGC", d, msg="Codon AGC was not found in the dictionary!")
        self.assertAlmostEqual(d["AGC"], 0.23993794345056002, places=4, msg="Incorrect probability of codon AGC!")
        self.assertIn("AUA", d, msg="Codon AUA was not found in the dictionary!")
        self.assertAlmostEqual(d["AUA"], 0.16906151748761036, places=4, msg="Incorrect probability of codon AUA!")
        self.assertIn("ACA", d, msg="Codon ACA was not found in the dictionary!")
        self.assertAlmostEqual(d["ACA"], 0.28418772983891855, places=4, msg="Incorrect probability of codon ACA!")
        self.assertIn("AAA", d, msg="Codon AAA was not found in the dictionary!")
        self.assertAlmostEqual(d["AAA"], 0.43404935110207155, places=4, msg="Incorrect probability of codon AAA!")
        self.assertIn("AGA", d, msg="Codon AGA was not found in the dictionary!")
        self.assertAlmostEqual(d["AGA"], 0.21465774794262568, places=4, msg="Incorrect probability of codon AGA!")
        self.assertIn("AUG", d, msg="Codon AUG was not found in the dictionary!")
        self.assertAlmostEqual(d["AUG"], 1.0, places=4, msg="Incorrect probability of codon AUG!")
        self.assertIn("ACG", d, msg="Codon ACG was not found in the dictionary!")
        self.assertAlmostEqual(d["ACG"], 0.11381188540055791, places=4, msg="Incorrect probability of codon ACG!")
        self.assertIn("AAG", d, msg="Codon AAG was not found in the dictionary!")
        self.assertAlmostEqual(d["AAG"], 0.5659506488979285, places=4, msg="Incorrect probability of codon AAG!")
        self.assertIn("AGG", d, msg="Codon AGG was not found in the dictionary!")
        self.assertAlmostEqual(d["AGG"], 0.21109127083138968, places=4, msg="Incorrect probability of codon AGG!")
        self.assertIn("GUU", d, msg="Codon GUU was not found in the dictionary!")
        self.assertAlmostEqual(d["GUU"], 0.18177011180348712, places=4, msg="Incorrect probability of codon GUU!")
        self.assertIn("GCU", d, msg="Codon GCU was not found in the dictionary!")
        self.assertAlmostEqual(d["GCU"], 0.26592161421413735, places=4, msg="Incorrect probability of codon GCU!")
        self.assertIn("GAU", d, msg="Codon GAU was not found in the dictionary!")
        self.assertAlmostEqual(d["GAU"], 0.4645424191930427, places=4, msg="Incorrect probability of codon GAU!")
        self.assertIn("GGU", d, msg="Codon GGU was not found in the dictionary!")
        self.assertAlmostEqual(d["GGU"], 0.1630865131632947, places=4, msg="Incorrect probability of codon GGU!")
        self.assertIn("GUC", d, msg="Codon GUC was not found in the dictionary!")
        self.assertAlmostEqual(d["GUC"], 0.23830637956135173, places=4, msg="Incorrect probability of codon GUC!")
        self.assertIn("GCC", d, msg="Codon GCC was not found in the dictionary!")
        self.assertAlmostEqual(d["GCC"], 0.39978112134364696, places=4, msg="Incorrect probability of codon GCC!")
        self.assertIn("GAC", d, msg="Codon GAC was not found in the dictionary!")
        self.assertAlmostEqual(d["GAC"], 0.5354575808069573, places=4, msg="Incorrect probability of codon GAC!")
        self.assertIn("GGC", d, msg="Codon GGC was not found in the dictionary!")
        self.assertAlmostEqual(d["GGC"], 0.33710935809444503, places=4, msg="Incorrect probability of codon GGC!")
        self.assertIn("GUA", d, msg="Codon GUA was not found in the dictionary!")
        self.assertAlmostEqual(d["GUA"], 0.11657741053350681, places=4, msg="Incorrect probability of codon GUA!")
        self.assertIn("GCA", d, msg="Codon GCA was not found in the dictionary!")
        self.assertAlmostEqual(d["GCA"], 0.2281212631716276, places=4, msg="Incorrect probability of codon GCA!")
        self.assertIn("GAA", d, msg="Codon GAA was not found in the dictionary!")
        self.assertAlmostEqual(d["GAA"], 0.42245266280361615, places=4, msg="Incorrect probability of codon GAA!")
        self.assertIn("GGA", d, msg="Codon GGA was not found in the dictionary!")
        self.assertAlmostEqual(d["GGA"], 0.24992165149690412, places=4, msg="Incorrect probability of codon GGA!")
        self.assertIn("GUG", d, msg="Codon GUG was not found in the dictionary!")
        self.assertAlmostEqual(d["GUG"], 0.46334609810165434, places=4, msg="Incorrect probability of codon GUG!")
        self.assertIn("GCG", d, msg="Codon GCG was not found in the dictionary!")
        self.assertAlmostEqual(d["GCG"], 0.10617600127058811, places=4, msg="Incorrect probability of codon GCG!")
        self.assertIn("GAG", d, msg="Codon GAG was not found in the dictionary!")
        self.assertAlmostEqual(d["GAG"], 0.5775473371963838, places=4, msg="Incorrect probability of codon GAG!")
        self.assertIn("GGG", d, msg="Codon GGG was not found in the dictionary!")
        self.assertAlmostEqual(d["GGG"], 0.24988247724535617, places=4, msg="Incorrect probability of codon GGG!")


@points('p07-01.6')
class TestProteinToMaxRNA(unittest.TestCase):

    def test_first(self):
        self.assertEqual(ProteinToMaxRNA().convert("LTPIQNRA"), "CUGACCCCCAUCCAGAACAGAGCC")

    def test_second(self):
        self.assertEqual(ProteinToMaxRNA().convert("ARNQIPTL"), "GCCAGAAACCAGAUCCCCACCCUG")

    def test_empty(self):
        self.assertEqual(ProteinToMaxRNA().convert(""), "")


@points('p07-01.7')
class TestRandomEvent(unittest.TestCase):

    def test_first(self):
        for _ in range(10):
            distribution = dict(zip("ACGT", [0.10, 0.35, 0.15, 0.40]))
            self.assertIn(random_event(distribution), "ACGT")

    def test_second(self):
        events = "First Second Third Fourth Fifth".split()
        for _ in range(10):
            distribution=dict(zip(events,
                              [0.5, 0.05, 0.20, 0.15, 0.10]))
            self.assertIn(random_event(distribution), events)

    def test_probs(self):
        probs = [0.10, 0.35, 0.15, 0.40]
        distribution = dict(zip("ACGT", probs))
        d = defaultdict(int)
        for _ in range(100000):
            d[random_event(distribution)] += 1/100000
        assert_allclose([d[c] for c in "ACGT"], probs, atol=0.1,
            err_msg="The probabilities do not seem to converge to the underlying distribution.")


@points('p07-01.8')
class TestProteinToRandomRNA(unittest.TestCase):

    @staticmethod
    def random_amino_acid_sequence(length):
        aas = list("*ACDEFGHIKLMNPQRSTVWY")
        result = np.random.choice(aas, length)
        return "".join(result)

    def test_first(self):
        p = ProteinToRandomRNA()
        result = p.convert("LTPIQNRA")
        self.assertEqual(len(p.convert("LTPIQNRA")), 24)

    def test_random(self):
        p = ProteinToRandomRNA()
        for length in range(100):
            s = TestProteinToRandomRNA.random_amino_acid_sequence(length)
            rna = p.convert(s)
            self.assertEqual(length*3, len(rna))
            nucs = set(rna)
            for nuc in nucs:
                self.assertIn(nuc, "ACGU")


@points('p07-01.9')
class TestSlidingWindow(unittest.TestCase):

    @staticmethod
    def random_nucleotide_sequence(length):
        nucs = list("ACGT")
        result = np.random.choice(nucs, length)
        return "".join(result)

    @staticmethod
    def is_subset(set1, set2):
        for element in set1:
            if element not in set2:
                return False
        return True

    def test_first(self):
        dicts=[{'T': 1, 'C': 1, 'A': 1, 'G': 1},
               {'T': 2, 'C': 1, 'A': 0, 'G': 1},
               {'T': 2, 'C': 0, 'A': 0, 'G': 2},
               {'T': 2, 'C': 1, 'A': 0, 'G': 1},
               {'T': 1, 'C': 1, 'A': 1, 'G': 1}]

        for d1, d2 in zip(dicts, sliding_window("ACGTTGCA", 4)):
            self.assertEqual(d1, d2)

    def test_random(self):
        for _ in range(10):
            s = TestSlidingWindow.random_nucleotide_sequence(100)
            for k in range(1, 20):
                for d in sliding_window(s, k):
                    self.assertEqual(sum(d.values()), k)
                    self.assertEqual(TestSlidingWindow.is_subset(d.keys(), "ACGT"), True)


@points('p07-01.10')
class TestContextList(unittest.TestCase):

    def test_first(self):
        k = 2
        s = "ATGATATCATCGACGATCTAG"
        d = context_list(s, k)

        self.assertEqual(len(d), 9)

        self.assertEqual(d["TC"], "AGT")
        self.assertEqual(d["CT"], "A")
        self.assertEqual(d["GA"], "TCT")
        self.assertEqual(d["TG"], "A")
        self.assertEqual(d["AC"], "G")
        self.assertEqual(d["TA"], "TG")
        self.assertEqual(d["CA"], "T")
        self.assertEqual(d["AT"], "GACCC")
        self.assertEqual(d["CG"], "AA")

    def test_random(self):
        n = 100
        for k in range(2, 5):
            s = TestSlidingWindow.random_nucleotide_sequence(n)
            d = context_list(s, k)
            self.assertLessEqual(len(d), n-k)
            self.assertEqual(sum([len(val) for key,val in d.items()]), n-k)


@points('p07-01.11')
class TestContextProbabilities(unittest.TestCase):

    def helper(self, d, context, nucleotide, probability):
        places = 3
        k = 2
        s = "ATGATATCATCGACGATGTAG"
        self.assertIn(context, d, msg="Context %s was not found in the result dictionary for parameters %s and %i!" % (context, s, k))
        self.assertIn(nucleotide, d[context],
                      msg="Nucleotide %s was not in the dictionary for context %s for parameters %s and %i!" % (nucleotide, context, s, k))
        self.assertAlmostEqual(d[context][nucleotide], probability, places=places,
                               msg="Incorrect probability for nucleotide %s in context %s!" % (nucleotide, context))

    def test_first(self):
        k = 2
        s = "ATGATATCATCGACGATGTAG"
        d = context_probabilities(s, k)

        self.helper(d, "AT", "G", 0.400000)
        self.helper(d, "AT", "A", 0.200000)
        self.helper(d, "AT", "C", 0.400000)
        self.helper(d, "TG", "A", 0.500000)
        self.helper(d, "TG", "T", 0.500000)
        self.helper(d, "GA", "T", 0.666667)
        self.helper(d, "GA", "C", 0.333333)
        self.helper(d, "TA", "T", 0.500000)
        self.helper(d, "TA", "G", 0.500000)
        self.helper(d, "TC", "A", 0.500000)
        self.helper(d, "TC", "G", 0.500000)
        self.helper(d, "CA", "T", 1.000000)
        self.helper(d, "CG", "A", 1.000000)
        self.helper(d, "AC", "G", 1.000000)
        self.helper(d, "GT", "A", 1.000000)

    def test_random(self):
        n = 100
        for k in range(5):
            s = TestSlidingWindow.random_nucleotide_sequence(n)
            d = context_probabilities(s, k)
            for context, d2 in d.items():
                self.assertAlmostEqual(sum(d2.values()), 1.0)

    def test_empty_context(self):
        k = 0
        n = 100
        s = TestSlidingWindow.random_nucleotide_sequence(n)
        d = context_probabilities(s, k)
        c = Counter(s)
        c = {nuc: count/n for nuc, count in c.items()} # Dictionary comprehension
        self.assertAlmostEqual(d[""], c, places=3)


@points('p07-01.12')
class TestGenerateMarkov(unittest.TestCase):
    zeroth = {'A': 0.2, 'C': 0.19, 'T': 0.31, 'G': 0.3}
    kth = {'GT': {'A': 1.0, 'C': 0.0, 'T': 0.0, 'G': 0.0},
           'CA': {'A': 0.0, 'C': 0.0, 'T': 1.0, 'G': 0.0},
           'TC': {'A': 0.5, 'C': 0.0, 'T': 0.0, 'G': 0.5},
           'GA': {'A': 0.0, 'C': 0.3333333333333333, 'T': 0.6666666666666666, 'G': 0.0},
           'TG': {'A': 0.5, 'C': 0.0, 'T': 0.5, 'G': 0.0},
           'AT': {'A': 0.2, 'C': 0.4, 'T': 0.0, 'G': 0.4},
           'TA': {'A': 0.0, 'C': 0.0, 'T': 0.5, 'G': 0.5},
           'AC': {'A': 0.0, 'C': 0.0, 'T': 0.0, 'G': 1.0},
           'CG': {'A': 1.0, 'C': 0.0, 'T': 0.0, 'G': 0.0}}

    def test_length(self):
        for n in range(100):
            try:
                mc = MarkovChain(TestGenerateMarkov.zeroth, TestGenerateMarkov.kth)
                s = mc.generate(n)
                self.assertEqual(len(s), n)
            except KeyError:
                pass

    def test_content(self):
        for n in range(100):
            try:
                mc = MarkovChain(TestGenerateMarkov.zeroth, TestGenerateMarkov.kth)
                s = mc.generate(n)
                self.assertTrue(TestSlidingWindow.is_subset(s, "ACGT"))
            except KeyError:
                pass

    def test_deterministic(self):
        n = 20
        seed = 1
        mc = MarkovChain(TestGenerateMarkov.zeroth, TestGenerateMarkov.kth)
        try:
            s1 = mc.generate(n, seed)
            s2 = mc.generate(n, seed)
            self.assertEqual(s1, s2,
                             msg="Generate method should always "\
                             "return the same result, if the same seed and length used!")
        except KeyError:
            pass

    def test_parameter_usage(self):
        zeroth = {"A": 1}
        kth = {"AA": {"A": 1}}
        mc = MarkovChain(zeroth, kth)
        self.assertEqual(mc.generate(20), "A"*20,
            msg=f"With zeroth: {zeroth} and kth: {kth}, the generated sequence should be {'A'*20}")


@points('p07-01.13')
class TestPseudoCounts(unittest.TestCase):

    def test_order_0(self):
        k = 0
        s = "ATGATATCATCGACGATGTAG"
        d2 = context_pseudo_probabilities(s, k)
        self.assertEqual(len(d2), 1)      # Number of 0-mers
        self.assertIn("", d2, msg="Only possible context for context length 0 is empty string!")
        d = d2[""]
        self.assertEqual(set(d), set(["A", "C", "G", "T"]),
                         msg="There should be exactly one probability for each of the four nucleotides!")
        places=3
        for nuc, prob in zip("ACGT", [0.32, 0.16, 0.24, 0.28]):
            self.assertAlmostEqual(d[nuc], prob, places=places,
                                   msg="Incorrect probability for nucleotide %s when context length is zero (s='%s')!" % (nuc, s))

    def test_order_2(self):
        k=2
        s="ATGATATCATCGACGATGTAG"
        d = context_pseudo_probabilities(s, k)
        self.assertEqual(len(d), 16)      # Number of 2-mers
        for context, d2 in d.items():
            self.assertEqual(len(d2), 4)  # Number of nucleotides per context
        places=3
        self.assertAlmostEqual(d["CT"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["CT"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["CT"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["CT"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["TC"]['C'], 0.166667, places=places)
        self.assertAlmostEqual(d["TC"]['T'], 0.166667, places=places)
        self.assertAlmostEqual(d["TC"]['G'], 0.333333, places=places)
        self.assertAlmostEqual(d["TC"]['A'], 0.333333, places=places)
        self.assertAlmostEqual(d["TA"]['T'], 0.333333, places=places)
        self.assertAlmostEqual(d["TA"]['C'], 0.166667, places=places)
        self.assertAlmostEqual(d["TA"]['G'], 0.333333, places=places)
        self.assertAlmostEqual(d["TA"]['A'], 0.166667, places=places)
        self.assertAlmostEqual(d["AA"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["AA"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["AA"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["AA"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["AT"]['C'], 0.333333, places=places)
        self.assertAlmostEqual(d["AT"]['T'], 0.111111, places=places)
        self.assertAlmostEqual(d["AT"]['G'], 0.333333, places=places)
        self.assertAlmostEqual(d["AT"]['A'], 0.222222, places=places)
        self.assertAlmostEqual(d["TG"]['T'], 0.333333, places=places)
        self.assertAlmostEqual(d["TG"]['C'], 0.166667, places=places)
        self.assertAlmostEqual(d["TG"]['G'], 0.166667, places=places)
        self.assertAlmostEqual(d["TG"]['A'], 0.333333, places=places)
        self.assertAlmostEqual(d["CG"]['C'], 0.166667, places=places)
        self.assertAlmostEqual(d["CG"]['T'], 0.166667, places=places)
        self.assertAlmostEqual(d["CG"]['G'], 0.166667, places=places)
        self.assertAlmostEqual(d["CG"]['A'], 0.500000, places=places)
        self.assertAlmostEqual(d["GG"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["GG"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["GG"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["GG"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["AC"]['C'], 0.200000, places=places)
        self.assertAlmostEqual(d["AC"]['T'], 0.200000, places=places)
        self.assertAlmostEqual(d["AC"]['G'], 0.400000, places=places)
        self.assertAlmostEqual(d["AC"]['A'], 0.200000, places=places)
        self.assertAlmostEqual(d["GC"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["GC"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["GC"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["GC"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["GT"]['C'], 0.200000, places=places)
        self.assertAlmostEqual(d["GT"]['T'], 0.200000, places=places)
        self.assertAlmostEqual(d["GT"]['G'], 0.200000, places=places)
        self.assertAlmostEqual(d["GT"]['A'], 0.400000, places=places)
        self.assertAlmostEqual(d["CA"]['T'], 0.400000, places=places)
        self.assertAlmostEqual(d["CA"]['C'], 0.200000, places=places)
        self.assertAlmostEqual(d["CA"]['G'], 0.200000, places=places)
        self.assertAlmostEqual(d["CA"]['A'], 0.200000, places=places)
        self.assertAlmostEqual(d["AG"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["AG"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["AG"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["AG"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["GA"]['T'], 0.428571, places=places)
        self.assertAlmostEqual(d["GA"]['C'], 0.285714, places=places)
        self.assertAlmostEqual(d["GA"]['G'], 0.142857, places=places)
        self.assertAlmostEqual(d["GA"]['A'], 0.142857, places=places)
        self.assertAlmostEqual(d["TT"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["TT"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["TT"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["TT"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["CC"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["CC"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["CC"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["CC"]['A'], 0.250000, places=places)

    def test_generation(self):
        k = 2
        n = 20
        s = "ACCGTT"
        ze = {"A": 0.25, "C": 0.25, "G": 0.25, "T": 0.25}
        mc = MarkovChain(ze, context_pseudo_probabilities(s, k), k)
        for _ in range(10):
            self.assertEqual(len(mc.generate(20)), 20,
                msg="Generating sequences should never fail when using pseudo probabilities.")


@points('p07-01.14')
class TestMarkovChainProbability(unittest.TestCase):
    kth = context_pseudo_probabilities("ATGATATCATCGACGATGTAG", 2)
    zeroth = context_pseudo_probabilities("ATGATATCATCGACGATGTAG", 0)[""]

    def test_length_one(self):
        mc = MarkovProb(2, TestMarkovChainProbability.zeroth, TestMarkovChainProbability.kth)
        try:
            mc.probability("A")
        except Exception:
            self.fail("Method probability does not work for strings of length 1!")

        self.assertAlmostEqual(mc.probability("A"), 0.32, places=10,
                               msg="Incorrect probability for sequence 'A'!")
        self.assertAlmostEqual(mc.probability("C"), 0.16, places=10,
                               msg="Incorrect probability for sequence 'C'!")
        self.assertAlmostEqual(mc.probability("G"), 0.24, places=10,
                               msg="Incorrect probability for sequence 'G'!")
        self.assertAlmostEqual(mc.probability("T"), 0.28, places=10,
                               msg="Incorrect probability for sequence 'T'!")

    def test_first(self):
        mc = MarkovProb(2, TestMarkovChainProbability.zeroth, TestMarkovChainProbability.kth)
        prob = mc.probability("ATGATATCATCGACGATGTAG")
        self.assertAlmostEqual(prob, 2.831270e-10, places=10)

    def test_random(self):
        mc = MarkovProb(2, TestMarkovChainProbability.zeroth, TestMarkovChainProbability.kth)
        for _ in range(100):
            s = TestSlidingWindow.random_nucleotide_sequence(20)
            prob = mc.probability(s)
            self.assertGreater(prob, 0.0)

    def test_uniform(self):
        u = dict.fromkeys("ACGT", 0.25)
        k = 2
        kth = {
            "".join(kmer): u
            for kmer in product("ACGT", repeat=k)
        }
        mp = MarkovProb(k, u, kth)
        for kmer in product("ACGT", repeat=4):
            self.assertAlmostEqual(mp.probability("".join(kmer)), 0.25**4)


@points('p07-01.15')
class TestMarkovChainLogProbability(unittest.TestCase):

    def test_first(self):
        mc = MarkovLog(2, TestMarkovChainProbability.zeroth, TestMarkovChainProbability.kth)
        prob = mc.log_probability("ATGATATCATCGACGATGTAG")
        self.assertAlmostEqual(prob, -3.171783e+01, places=5)

    def test_random(self):
        mc = MarkovLog(2, TestMarkovChainProbability.zeroth, TestMarkovChainProbability.kth)
        for _ in range(100):
            s = TestSlidingWindow.random_nucleotide_sequence(20)
            prob = mc.log_probability(s)
            self.assertLessEqual(prob, 0.0)

    def test_uniform(self):
        u = dict.fromkeys("ACGT", 0.25)
        k = 2
        kth = {
            "".join(kmer): u
            for kmer in product("ACGT", repeat=k)
        }
        mc = MarkovLog(k, u, kth)
        n = 4
        for kmer in product("ACGT", repeat=n):
            self.assertAlmostEqual(mc.log_probability("".join(kmer)), -2*n)


@points('p07-01.16')
class TestLowSpaceRequirement(unittest.TestCase):

    def test_first(self):
        k=2
        s="ATGATATCATCGACGATGTAG"
        d = better_context_probabilities(s, k)
        self.assertEqual(len(d), 16)      # Number of 2-mers
        for context, d2 in d.items():
            self.assertEqual(len(d2), 4)  # Number of nucleotides per context
        places=3
        self.assertAlmostEqual(d["CT"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["CT"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["CT"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["CT"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["TC"]['C'], 0.166667, places=places)
        self.assertAlmostEqual(d["TC"]['T'], 0.166667, places=places)
        self.assertAlmostEqual(d["TC"]['G'], 0.333333, places=places)
        self.assertAlmostEqual(d["TC"]['A'], 0.333333, places=places)
        self.assertAlmostEqual(d["TA"]['T'], 0.333333, places=places)
        self.assertAlmostEqual(d["TA"]['C'], 0.166667, places=places)
        self.assertAlmostEqual(d["TA"]['G'], 0.333333, places=places)
        self.assertAlmostEqual(d["TA"]['A'], 0.166667, places=places)
        self.assertAlmostEqual(d["AA"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["AA"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["AA"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["AA"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["AT"]['C'], 0.333333, places=places)
        self.assertAlmostEqual(d["AT"]['T'], 0.111111, places=places)
        self.assertAlmostEqual(d["AT"]['G'], 0.333333, places=places)
        self.assertAlmostEqual(d["AT"]['A'], 0.222222, places=places)
        self.assertAlmostEqual(d["TG"]['T'], 0.333333, places=places)
        self.assertAlmostEqual(d["TG"]['C'], 0.166667, places=places)
        self.assertAlmostEqual(d["TG"]['G'], 0.166667, places=places)
        self.assertAlmostEqual(d["TG"]['A'], 0.333333, places=places)
        self.assertAlmostEqual(d["CG"]['C'], 0.166667, places=places)
        self.assertAlmostEqual(d["CG"]['T'], 0.166667, places=places)
        self.assertAlmostEqual(d["CG"]['G'], 0.166667, places=places)
        self.assertAlmostEqual(d["CG"]['A'], 0.500000, places=places)
        self.assertAlmostEqual(d["GG"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["GG"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["GG"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["GG"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["AC"]['C'], 0.200000, places=places)
        self.assertAlmostEqual(d["AC"]['T'], 0.200000, places=places)
        self.assertAlmostEqual(d["AC"]['G'], 0.400000, places=places)
        self.assertAlmostEqual(d["AC"]['A'], 0.200000, places=places)
        self.assertAlmostEqual(d["GC"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["GC"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["GC"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["GC"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["GT"]['C'], 0.200000, places=places)
        self.assertAlmostEqual(d["GT"]['T'], 0.200000, places=places)
        self.assertAlmostEqual(d["GT"]['G'], 0.200000, places=places)
        self.assertAlmostEqual(d["GT"]['A'], 0.400000, places=places)
        self.assertAlmostEqual(d["CA"]['T'], 0.400000, places=places)
        self.assertAlmostEqual(d["CA"]['C'], 0.200000, places=places)
        self.assertAlmostEqual(d["CA"]['G'], 0.200000, places=places)
        self.assertAlmostEqual(d["CA"]['A'], 0.200000, places=places)
        self.assertAlmostEqual(d["AG"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["AG"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["AG"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["AG"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["GA"]['T'], 0.428571, places=places)
        self.assertAlmostEqual(d["GA"]['C'], 0.285714, places=places)
        self.assertAlmostEqual(d["GA"]['G'], 0.142857, places=places)
        self.assertAlmostEqual(d["GA"]['A'], 0.142857, places=places)
        self.assertAlmostEqual(d["TT"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["TT"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["TT"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["TT"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["CC"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["CC"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["CC"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["CC"]['A'], 0.250000, places=places)


@points('p07-01.17')
class TestSampleFromConcatenation(unittest.TestCase):

    def test_length_one(self):
        k=2
        s="ATGATATCATCGACGATGTAG"
        seed=0
        mc = SimpleMarkovChain(s, k)
        t = mc.generate(1, seed)
        self.assertEqual(len(t), 1, msg="generate does not work if string of length one is requested!")

    def test_deterministic(self):
        k=2
        s="ATGATATCATCGACGATGTAG"
        seed=0
        mc = SimpleMarkovChain(s, k)
        s1 = mc.generate(40, seed)
        s2 = mc.generate(40, seed)
        self.assertEqual(s1, s2, msg="Generate method should always return the same result, if the same seed and length used!")

    def test_second(self):
        s="ATGATATCATCGACGATGTAG"
        seed=0
        for n in range(40):
            for k in range(4):
                mc = SimpleMarkovChain(s, k)
                s2 = mc.generate(n, seed)
                self.assertEqual(len(s2), n, msg="Expected a string of length %i from the 'generate' method!" % n)
                self.assertTrue(TestSlidingWindow.is_subset(s2, "ACGT"), msg="The generated string %s contains non-nucleotide characters!" % s2)


@points('p07-01.18')
class TestKmerIndex(unittest.TestCase):

    def test_first(self):
        s = "ATGATATCATCGACGATGTAG"
        n = len(s)
        for k in range(4):
            index = kmer_index(s, k)
            positions = []
            for context, pos_lst in index.items():
                positions.extend(pos_lst)
            self.assertEqual(len(positions), n - k + 1)
            positions.sort()
            self.assertSequenceEqual(positions, range(n - k + 1))


@points('p07-01.19')
class TestKullbackLeibler(unittest.TestCase):

    def test_first(self):
        p = dict(zip("ACGT", [0.25]*4))
        self.assertAlmostEqual(kullback_leibler(p, p), 0.0, places=3)

    def test_second(self):
        p = dict(zip("ACGT", [1.0, 0.0, 0.0, 0.0]))
        q = dict(zip("ACGT", [0.25]*4))
        self.assertAlmostEqual(kullback_leibler(p, q), 2.0, places=3)

    def test_exception(self):
        p = dict(zip("ACGT", [1.0, 0.0, 0.0, 0.0]))
        q = dict(zip("ACGT", [0.25]*4))
        self.assertRaises(ZeroDivisionError, kullback_leibler, q, p)

    def test_single(self):
        p = { "A" : 1.0 }
        self.assertAlmostEqual(kullback_leibler(p, p), 0.0, places=3)


@points('p07-01.20')
class StationaryDistribution(unittest.TestCase):

    def test_first(self):
        transition=np.array([[0.3, 0, 0.7, 0],
                             [0, 0.4, 0, 0.6],
                             [0.35, 0, 0.65, 0],
                             [0, 0.2, 0, 0.8]])
        distributions = get_stationary_distributions(transition)
        assert_allclose(distributions[0], [0.33333333, 0., 0.66666667,  0], atol=1e-04)
        assert_allclose(distributions[1], [ 0., 0.25, 0., 0.75], atol=1e-04)

@points('p07-01.21')
class StationaryInitialDistribution(unittest.TestCase):

    def test_correctness(self):
        initial = [0.00, 0.25, 0.00, 0.75]
        transition=np.array([[0.3, 0, 0.7, 0],
                             [0, 0.4, 0, 0.6],
                             [0.35, 0, 0.65, 0],
                             [0, 0.2, 0, 0.8]])
        results = list(kl_divergences(initial, transition))
        self.assertEqual(len(results), 5, msg="Expected results for 5 different prefix lengths")
        for i in range(1, len(results)):
            self.assertGreater(results[i-1][1], results[i][1], msg="divergences should converge towards 0.")


@points('p07-01.22')
class EquilibriumDistribution(unittest.TestCase):

    def test_eqd_correctness(self):
        transition = np.array([[0.3, 0.1, 0.5, 0.1],
                               [0.2, 0.3, 0.15, 0.35],
                               [0.25, 0.15, 0.2, 0.4],
                               [0.35, 0.2, 0.4, 0.05]])
        stationary_distributions = get_stationary_distributions(transition)
        self.assertEqual(len(stationary_distributions), 1, msg="There should be only one stationary distribution.")
        equilibrium_distribution = stationary_distributions[0]
        assert_allclose(equilibrium_distribution, [0.27803345, 0.17353238, 0.32035021, 0.22808396], atol=1e-04,
            err_msg="The equilibrium distribution seems to be wrong.")

    def test_convergence(self):
        transition = np.array([[0.3, 0.1, 0.5, 0.1],
                               [0.2, 0.3, 0.15, 0.35],
                               [0.25, 0.15, 0.2, 0.4],
                               [0.35, 0.2, 0.4, 0.05]])
        equilibrium_distribution = get_stationary_distributions(transition)[0]
        res = list(main(transition, equilibrium_distribution))
        eqs = 0
        for a, b in zip(res[0][0], res[1][0]):
            if np.abs(a - b) < 0.05:
                eqs += 1
        self.assertLess(eqs, 4, msg="initial random distributins were very similar.")
        assert_allclose(res[0][1][-1][1], equilibrium_distribution, atol=0.1,
            err_msg="First distribution did not seem to converge that strongly.")
        assert_allclose(res[1][1][-1][1], equilibrium_distribution, atol=0.1,
            err_msg="First distribution did not seem to converge that strongly.")


if __name__ == '__main__':
    unittest.main()
