class Sizes:
    width = 800
    height = 600
    margin = 10
    grid = margin
    halfMargin = margin // 2
    halfWidthPadding = width // margin // 2

    def center_point():
        import primitif.utility as utility
        utility.convert_to_cartesian(
            Sizes.size_grid(0),
            Sizes.size_grid(0),
            Sizes.width,
            Sizes.height,
            Sizes.margin
        )

    def size_grid(panjang):
        return panjang * Sizes.grid

    def half_widht():
        return Sizes.width // 2
