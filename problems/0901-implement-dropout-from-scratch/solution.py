import torch

def dropout(x: torch.Tensor, p: float, training: bool) -> torch.Tensor:
    # TODO: implement inverted dropout
    if training == False:
        return x
    elif  p == 0:
        return x
    if p == 1.0:
        return torch.zeros_like(x)

    mask = (torch.rand_like(x) >= p).float()

    return (x * mask) / (1.0 - p)