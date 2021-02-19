<xsl:stylesheet version="1.0">
    <xsl:output method="xml"/>
    <xsl:template match="svg:svg">
        <xsl:copy>
            <xsl:copy-of select="svg:metadata|svg:defs|sodipodi:namedview"/>
            <xsl:element name="svg:g">
                <xsl:attribute name="transform">
                    <xsl:value-of select="concat(concat('scale(',$scale),')')"/>
                </xsl:attribute>
                <xsl:copy-of select="*[not(svg:metadata|svg:defs|sodipodi:namedview)]"/>
            </xsl:element>
        </xsl:copy>
    </xsl:template>
</xsl:stylesheet>