import numpy as np
from animations.spacetime_grid import create_spacetime_grid

import astropy.constants as const
import astropy.units as u


def hawking_temperature(mass):

    M = mass * u.kg

    T = (

        const.hbar
        * const.c**3

        /

        (

            8
            * np.pi
            * const.G
            * M
            * const.k_B

        )

    )

    return T.to(

        u.MeV,

        equivalencies=u.temperature_energy()

    )


def schwarzschild_radius(mass):

    M = mass * u.kg

    r = (

        2

        * const.G

        * M

        /

        const.c**2

    )

    return r.to(u.m)


def evaporation_lifetime(mass):

    M = mass * u.kg

    t = (

        5120

        * np.pi

        * const.G**2

        * M**3

        /

        (

            const.hbar

            * const.c**4

        )

    )

    return t.to(u.year)
