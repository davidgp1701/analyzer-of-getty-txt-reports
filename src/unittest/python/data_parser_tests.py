# Under Apache 2.0 license
# Copyright - David García Pérez 2017

import unittest
import data_parser as parser


class DataParserTests(unittest.TestCase):
    """Verifies that we are able to parse correclty all Getty reports"""

    example_file_1 = 'src/unittest/resources/201601-123456-all.txt'

    def test_parse_monthly(self):
        """ Verifes that we are able to parse a monthly report """

        rows = parser.parse_monthly_file(self.example_file_1)

        self.assertEquals('David García Pérez', rows[0]['Name'])
        self.assertEquals('123456', rows[0]['Contact ID'])
        self.assertEquals('1234567;Flickr;David Garcfa PTrez 123456', rows[0]['Contract Name'])
        self.assertEquals('ene-2016', rows[0]['Royalty Month'])
        self.assertEquals('12345678-123456789', rows[0]['Invoice Number'])
        self.assertEquals('04-ene-2016', rows[0]['Sales Date'])
        self.assertEquals('Moment Open', rows[0]['Collection'])
        self.assertEquals('US SALES', rows[0]['Sale Region'])
        self.assertEquals('Premium Access Time Limited', rows[0]['Product Type'])
        self.assertEquals('', rows[0]['Notes'])
        self.assertEquals('', rows[0]['File Size'])
        self.assertEquals('', rows[0]['Agent'])
        self.assertEquals('XXXXX YYYYY ZZZZZ XA', rows[0]['Customer Name'])
        self.assertEquals('David Garcia Perez', rows[0]['Credit Line'])
        self.assertEquals('123456789', rows[0]['Asset Number'])
        self.assertEquals('20100606_illas_cies_kdd_phosgalicia_0038.jpg', rows[0]['Alternate Asset Number'])
        self.assertEquals('123456789-Illas Cíes', rows[0]['Asset Description'])
        self.assertEquals('', rows[0]['Rights: Industry'])
        self.assertEquals('3/13/15 - 3/12/16Publishing-Web, Territory: North America. Editorial and in context Mobile and self-promotional rights granted for Licensee\'s website. Limited Syndication rights granted.Reproduction rights limited to the term of the agreement. Archival rights in perpetuity in context of original use.', rows[0]['Rights Usage'])
        self.assertEquals('Limited to terms of the Premium Access agreement', rows[0]['Rights: Use Territory/Duration'])
        self.assertEquals('NEW YORK', rows[0]['Sales Territory'])
        self.assertEquals('1.000000000', rows[0]['Percent of Product'])
        self.assertEquals('Getty', rows[0]['Purchase from Site'])
        self.assertEquals('15.000000000', rows[0]['License Fee in USD'])
        self.assertEquals('0.200000000', rows[0]['Royalty Rate'])
        self.assertEquals('3.000000000', rows[0]['Gross Royalty in USD'])
        self.assertEquals('2016-03-25T00:00:00', rows[0]['Royalty Pay Date'])
        self.assertEquals('0.000000000', rows[0]['Contributors Net payment (summary for full stmt)'])
        self.assertEquals('USD', rows[0]['Currency'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_CarryForwardNegativeEarnings'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_CarryForwardNegativePrevious'])
        self.assertEquals('100.000000000', rows[0]['StatementSummary_ContributorsPercentage'])
        self.assertEquals('100.000000000', rows[0]['StatementSummary_ExchangeRate'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_NewAdvance'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_OpeningBalance'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_US_ContributorsShare'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_US_Deductions'])
        self.assertEquals('3.006800000', rows[0]['StatementSummary_US_Gross'])
        self.assertEquals('3.014200000', rows[0]['StatementSummary_US_MinimumNotMetCarriedForward'])
        self.assertEquals('3.006800000', rows[0]['StatementSummary_US_Net'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_US_NetPayment'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_US_NetPaymentInCurrency'])
        self.assertEquals('0.007400000', rows[0]['StatementSummary_US_PaymentCarriedForward'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_US_EstimatedTaxOnAmount'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_US_EstimatedTaxOnAmountInCurrency'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_NonUS_ContributorsShare'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_NonUS_Deductions'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_NonUS_Gross'])
        self.assertEquals('0.973200000', rows[0]['StatementSummary_NonUS_MinimumNotMetCarriedForward'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_NonUS_NetEarnings'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_NonUS_Net'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_NonUS_NetPaymentInCurrency'])
        self.assertEquals('0.973200000', rows[0]['StatementSummary_NonUS_PaymentCarriedForward'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_NonUS_EstimatedTaxOnAmount'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_NonUS_EstimatedTaxOnAmountInCurrency'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_Totals_ClosingBalance'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_Totals_Deductions'])
        self.assertEquals('3.006800000', rows[0]['StatementSummary_Totals_Gross'])
        self.assertEquals('3.987400000', rows[0]['StatementSummary_Totals_MinimumNotMetCarriedForward'])
        self.assertEquals('3.987400000', rows[0]['StatementSummary_Totals_NetEarnings'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_Totals_NetPayment'])
        self.assertEquals('0.980600000', rows[0]['StatementSummary_Totals_PaymentCarriedForward'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_Totals_EstimatedTaxOnAmount'])
        self.assertEquals('0.000000000', rows[0]['StatementSummary_Totals_EstimatedTaxOnAmountInCurrency'])
