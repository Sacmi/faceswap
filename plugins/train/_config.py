#!/usr/bin/env python3
""" Default configurations for models """

import logging

from lib.config import FaceswapConfig

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class Config(FaceswapConfig):
    """ Config File for Models """

    def set_defaults(self):
        """ Set the default values for config """
        logger.debug("Setting defaults")
        # << GLOBAL OPTIONS >> #
        section = "global"
        self.add_section(title=section,
                         info="Options that apply to all models")
        self.add_item(
            section=section, title="dssim_loss", datatype=bool, default=True,
            info="Use DSSIM for Loss rather than Mean Absolute Error\n"
                 "May increase overall quality.\nChoose from: True, False")

        # << ORIGINAL MODEL OPTIONS >> #
        section = "original"
        self.add_section(title=section,
                         info="Original Faceswap Model")
        self.add_item(
            section=section, title="lowmem", datatype=bool, default=False,
            info="Lower memory mode. Set to 'True' if having issues with VRAM useage.\nNB: Models "
                 "with a changed lowmem mode are not compatible with each other."
                 "\nChoose from: True, False")
        self.add_item(
            section=section, title="input_size", datatype=int, default=64,
            info="Resolution (in pixels) of the image to train on.\n"
                 "BE AWARE Larger resolution will dramatically increase"
                 "VRAM requirements.\n"
                 "Make sure your resolution is divisible by 64 "
                 "(e.g. 64, 128, 256 etc.)")

        # << ORIGINAL HIRES MODEL OPTIONS >> #
        section = "original_hires"
        self.add_section(title=section,
                         info="Higher resolution version of the Original "
                              "Model")
        self.add_item(
            section=section, title="encoder_type", datatype=str, default="ORIGINAL",
            info="Encoder type to use. Choose from:\n"
                 "ORIGINAL: Basic encoder for this model type\n"
                 "STANDARD: New, balanced encoder. More memory consuming\n"
                 "HIGHRES: High resolution tensors optimized encoder: 176x+")
        self.add_item(
            section=section, title="nodes", datatype=int, default=1024,
            info="Number of nodes for decoder. Don't change this unless you "
                 "know what you are doing!")
        self.add_item(
            section=section, title="complexity_encoder", datatype=int, default=128,
            info="Encoder Convolution Layer Complexity. sensible ranges: "
                 "128 to 160")
        self.add_item(
            section=section, title="complexity_decoder_a", datatype=int, default=384,
            info="Decoder A Complexity. Only applicable for STANDARD and "
                 "ORIGINAL encoders")
        self.add_item(
            section=section, title="complexity_decoder_b", datatype=int, default=512,
            info="Decoder B Complexity. Only applicable for STANDARD and "
                 "ORIGINAL encoders")
        self.add_item(
            section=section, title="subpixel_upscaling", datatype=bool, default=False,
            info="Might increase upscaling quality at cost of VRAM")
        self.add_item(
            section=section, title="input_size", datatype=int, default=128,
            info="Resolution (in pixels) of the image to train on.\n"
                 "BE AWARE Larger resolution will dramatically increase"
                 "VRAM requirements.\n"
                 "Make sure your resolution is divisible by 64 "
                 "(e.g. 64, 128, 256 etc.)")

        # << DFAKER MODEL OPTIONS >> #
        section = "dfaker"
        self.add_section(title=section,
                         info="Dfaker Model (Adapted from https://github.com/dfaker/df)")
        self.add_item(
            section=section, title="input_size", datatype=int, default=64,
            info="Resolution (in pixels) of the image to train on.\n"
                 "BE AWARE Larger resolution will dramatically increase"
                 "VRAM requirements.\n"
                 "Make sure your resolution is divisible by 64 "
                 "(e.g. 64, 128, 256 etc.)")
        self.add_item(
            section=section, title="alignments_format", datatype=str, default="json",
            info="Dfaker model requires the alignments for your training "
                 "images to be avalaible within the FACES folder.\nIt should "
                 "be named 'alignments.<file extension>' (eg. "
                 "alignments.json)."
                 "\nChoose from: 'json', 'pickle' or 'yaml'")
        self.add_item(
            section=section, title="mask_type", datatype=str, default="dfaker",
            info="The mask to be used for training."
                 "\nChoose from: 'dfaker' or 'dfl_full'")
        self.add_item(
            section=section, title="dssim_mask_loss", datatype=bool, default=True,
            info="Use DSSIM loss for Mask rather than Mean Absolute Error\n"
                 "May increase overall quality.\nChoose from: True, False")
        self.add_item(
            section=section, title="penalized_mask_loss", datatype=bool, default=True,
            info="Use Penalized loss for Mask. Can stack with DSSIM.\n"
                 "May increase overall quality.\nChoose from: True, False")

        # << DFL MODEL OPTIONS >> #
        section = "dfl_h128"
        self.add_section(title=section,
                         info="DFL H128 Model (Adapted from https://github.com/iperov/DeepFaceLab")
        self.add_item(
            section=section, title="lowmem", datatype=bool, default=False,
            info="Lower memory mode. Set to 'True' if having issues with VRAM useage.\nNB: Models "
                 "with a changed lowmem mode are not compatible with each other."
                 "\nChoose from: True, False")
        self.add_item(
            section=section, title="alignments_format", datatype=str, default="json",
            info="DFL-H128 model requires the alignments for your training "
                 "images to be avalaible within the FACES folder.\nIt should "
                 "be named 'alignments.<file extension>' (eg. "
                 "alignments.json)."
                 "\nChoose from: 'json', 'pickle' or 'yaml'")
        self.add_item(
            section=section, title="input_size", datatype=int, default=128,
            info="Resolution (in pixels) of the image to train on.\n"
                 "BE AWARE Larger resolution will dramatically increase"
                 "VRAM requirements.\n"
                 "Make sure your resolution is divisible by 64 "
                 "(e.g. 64, 128, 256 etc.)")
        self.add_item(
            section=section, title="mask_type", datatype=str, default="dfl_full",
            info="The mask to be used for training."
                 "\nChoose from: 'dfaker' or 'dfl_full'")
        self.add_item(
            section=section, title="dssim_mask_loss", datatype=bool, default=True,
            info="Use DSSIM loss for Mask rather than Mean Absolute Error\n"
                 "May increase overall quality.\nChoose from: True, False")
        self.add_item(
            section=section, title="penalized_mask_loss", datatype=bool, default=True,
            info="Use Penalized loss for Mask. Can stack with DSSIM.\n"
                 "May increase overall quality.\nChoose from: True, False")
