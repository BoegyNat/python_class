import uuid

def writeHeadColumn(count):
    x_base = 320
    y_header = 20
    y_subheader = 40
    width_header = 100
    width_sub = 50
    height = 20

    output = []

    for i in range(1, count + 1):
        x_offset = (i - 1) * (width_sub * 2)

        field_name = f"orderTypeName{i}"

        # Header field
        output.append(f'''<textField textAdjust="ScaleFont" isBlankWhenNull="true" >
    <reportElement x="{x_base + x_offset}" y="{y_header}" width="{width_header}" height="{height}" uuid="{uuid.uuid4()}"/>
    <box>
        <pen lineWidth="0.25"/>
        <topPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <leftPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <bottomPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <rightPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
    </box>
    <textElement textAlignment="Center" verticalAlignment="Middle">
        <font fontName="TH SarabunPSK"/>
        <paragraph leftIndent="5" rightIndent="5"/>
    </textElement>
    <textFieldExpression><![CDATA[$F{{{field_name}}}]]></textFieldExpression>
</textField>''')

        # Sub-header: จำนวนเงิน
        output.append(f'''<textField>
    <reportElement x="{x_base + x_offset}" y="{y_subheader}" width="{width_sub}" height="{height}" uuid="{uuid.uuid4()}"/>
    <box>
        <pen lineWidth="0.25"/>
        <topPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <leftPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <bottomPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <rightPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
    </box>
    <textElement textAlignment="Center" verticalAlignment="Middle">
        <font fontName="TH SarabunPSK"/>
        <paragraph leftIndent="5" rightIndent="5"/>
    </textElement>
    <textFieldExpression><![CDATA["จำนวนเงิน"]]></textFieldExpression>
</textField>''')

        # Sub-header: ภาษี
        output.append(f'''<textField>
    <reportElement x="{x_base + x_offset + width_sub}" y="{y_subheader}" width="{width_sub}" height="{height}" uuid="{uuid.uuid4()}"/>
    <box>
        <pen lineWidth="0.25"/>
        <topPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <leftPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <bottomPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <rightPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
    </box>
    <textElement textAlignment="Center" verticalAlignment="Middle">
        <font fontName="TH SarabunPSK"/>
        <paragraph leftIndent="5" rightIndent="5"/>
    </textElement>
    <textFieldExpression><![CDATA["ภาษี"]]></textFieldExpression>
</textField>''')

    return "\n\n".join(output)




def writeDetailColumn(count):
    x_base = 320
    width = 50
    height = 30
    y = 0
    pattern = "#,##0.00"
    connection_id = "5e50b28a-1d1e-4f06-affe-01ebddcee68d"

    output = []

    for i in range(1, count + 1):
        x_total = x_base + (i - 1) * 2 * width
        x_tax = x_total + width

        total_field = f"total{i}"
        tax_field = f"tax{i}"

        # total field
        output.append(f'''<textField textAdjust="ScaleFont" isBlankWhenNull="true" pattern="{pattern}">
    <reportElement x="{x_total}" y="{y}" width="{width}" height="{height}" uuid="{uuid.uuid4()}">
        <property name="com.jaspersoft.studio.spreadsheet.connectionID" value="{connection_id}"/>
    </reportElement>
    <box>
        <topPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <leftPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <bottomPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <rightPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
    </box>
    <textElement textAlignment="Right" verticalAlignment="Middle">
        <font fontName="TH SarabunPSK"/>
        <paragraph leftIndent="5" rightIndent="5"/>
    </textElement>
    <textFieldExpression><![CDATA[$F{{{total_field}}}]]></textFieldExpression>
</textField>''')

        # tax field
        output.append(f'''<textField textAdjust="ScaleFont" isBlankWhenNull="true" pattern="{pattern}">
    <reportElement x="{x_tax}" y="{y}" width="{width}" height="{height}" uuid="{uuid.uuid4()}">
        <property name="com.jaspersoft.studio.spreadsheet.connectionID" value="{connection_id}"/>
    </reportElement>
    <box>
        <topPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <leftPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <bottomPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <rightPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
    </box>
    <textElement textAlignment="Right" verticalAlignment="Middle">
        <font fontName="TH SarabunPSK"/>
        <paragraph leftIndent="5" rightIndent="5"/>
    </textElement>
    <textFieldExpression><![CDATA[$F{{{tax_field}}}]]></textFieldExpression>
</textField>''')

    return "\n\n".join(output)


def writeSumColumn(count):
    x_base = 320
    width = 50
    height = 30
    y = 0

    output = []

    for i in range(1, count + 1):
        x_total = x_base + (i - 1) * 2 * width
        x_tax = x_total + width

        total_var = f"totalSum{i}"
        tax_var = f"taxSum{i}"

        # totalSum field
        output.append(f'''<textField textAdjust="ScaleFont" isBlankWhenNull="true" pattern="#,##0.00">
    <reportElement x="{x_total}" y="{y}" width="{width}" height="{height}" uuid="{uuid.uuid4()}"/>
    <box rightPadding="3">
        <pen lineWidth="0.25"/>
        <topPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <leftPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <bottomPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <rightPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
    </box>
    <textElement textAlignment="Right" verticalAlignment="Middle">
        <font fontName="TH SarabunPSK"/>
        <paragraph leftIndent="5" rightIndent="5"/>
    </textElement>
    <textFieldExpression><![CDATA[$V{{{total_var}}}]]></textFieldExpression>
</textField>''')

        # taxSum field
        output.append(f'''<textField textAdjust="ScaleFont" isBlankWhenNull="true" pattern="#,##0.00">
    <reportElement x="{x_tax}" y="{y}" width="{width}" height="{height}" uuid="{uuid.uuid4()}"/>
    <box rightPadding="3">
        <pen lineWidth="0.25"/>
        <topPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <leftPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <bottomPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
        <rightPen lineWidth="0.25" lineStyle="Solid" lineColor="#000000"/>
    </box>
    <textElement textAlignment="Right" verticalAlignment="Middle">
        <font fontName="TH SarabunPSK"/>
        <paragraph leftIndent="5" rightIndent="5"/>
    </textElement>
    <textFieldExpression><![CDATA[$V{{{tax_var}}}]]></textFieldExpression>
</textField>''')

    return "\n\n".join(output)


def writeFieldAndVariable(count):
    fields = []
    variables = []

    for i in range(1, count + 1):
        fields.append(f'''<field name="orderTypeName{i}" class="java.lang.String"/>''')
        fields.append(f'''<field name="total{i}" class="java.lang.Double"/>''')
        fields.append(f'''<field name="tax{i}" class="java.lang.Double"/>''')

        variables.append(f'''<variable name="totalSum{i}" class="java.lang.Double" calculation="Sum">
    <variableExpression><![CDATA[$F{{total{i}}}]]></variableExpression>
</variable>''')

        variables.append(f'''<variable name="taxSum{i}" class="java.lang.Double" calculation="Sum">
    <variableExpression><![CDATA[$F{{tax{i}}}]]></variableExpression>
</variable>''')

    return "\n".join(fields + [""] + variables)




with open("output_columns.txt", "w", encoding="utf-8") as f:
    f.write(writeHeadColumn(75))
    # f.write(writeDetailColumn(75))
    # f.write(writeSumColumn(75))
    # f.write(writeFieldAndVariable(75))
print("Export success ✅ => output_columns.txt")
