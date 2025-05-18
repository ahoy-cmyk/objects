"""Generative mesh creation from natural language.

This module provides a placeholder interface for creating meshes from
arbitrary text descriptions using external models such as Shap-E.  The
function returns ``None`` if the required libraries are unavailable.
"""

from typing import Optional
import logging

try:
    import trimesh
except ImportError:  # pragma: no cover - trimesh is optional
    trimesh = None

try:
    import torch
    from shap_e.diffusion.sample import sample_latents
    from shap_e.diffusion.gaussian_diffusion import diffusion_from_config
    from shap_e.util.notebooks import decode_latent_mesh
    from shap_e.models.download import load_model
    from shap_e.util import download
except Exception:  # pragma: no cover - shap-e is optional
    torch = None


# Config paths used by Shap-E when installed
CONFIG_NAME = "configs/image_and_text.json"
MODEL_NAME = "text300M"


def generate_from_text(text: str) -> Optional["trimesh.Trimesh"]:
    """Attempt to generate a mesh from an arbitrary text description.

    This is a thin wrapper around the Shap-E example pipeline. It requires
    the ``shap_e`` package and ``torch``. If these dependencies are
    unavailable, the function returns ``None``.
    """
    if torch is None or trimesh is None:
        logging.warning("Generative dependencies not available")
        return None

    device = "cuda" if torch.cuda.is_available() else "cpu"
    try:
        model = load_model(MODEL_NAME, device)
        diffusion = diffusion_from_config(download.get_config(CONFIG_NAME))
        latents = sample_latents(
            batch_size=1,
            model=model,
            diffusion=diffusion,
            guidance_scale=15.0,
            model_kwargs=dict(prompts=[text]),
            progress=False,
            device=device,
        )
        mesh = decode_latent_mesh(latents[0]).tri_mesh()
        return mesh
    except Exception as exc:  # pragma: no cover - runtime errors
        logging.error("Generative model failed: %s", exc)
        return None
