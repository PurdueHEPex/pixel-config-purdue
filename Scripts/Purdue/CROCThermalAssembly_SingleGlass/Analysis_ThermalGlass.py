"""Analysis."""

import statistics
import ROOT


def strIntRound(x):
    """Round to the nearest integer."""
    return str(int(round(x, 0)))


file = open(r"C:\Users\das69\pixel-gantry-control\Logs\LOG_Assembly_CROC_SingleGlass_DataGeneration.txt")
line = file.readline()

v_DeltaDeltaX = []
v_AvgDeltaY = []


h_DeltaDeltaX = ROOT.TH1F(
    "h_DeltaDeltaX",
    "; Angular Opening #Delta#deltax between Thermal mockup and Piece of Glass",
    10, -0.1, 0.1)
h_AvgDeltaY = ROOT.TH1F(
    "h_AvgDeltaY",
    "; Slide Average(#deltay) between Thermal mockup and Piece of Glass",
    10, -.3, 0.3)

while line:
    line = file.readline()
    line = line[27:]
    if "Meaningful Values" in line:
        line = file.readline()
        if "Delta(delta(X))" in line:
            deltaDeltaX = float(line[line.find("):")+3:])
            v_DeltaDeltaX.append(deltaDeltaX)
            h_DeltaDeltaX.Fill(deltaDeltaX)
            line = file.readline()
        if "Avg(delta(Y))" in line:
            avgDeltaY = float(line[line.find("):")+3:])
            v_AvgDeltaY.append(avgDeltaY)
            h_AvgDeltaY.Fill(avgDeltaY)



c_DeltaDeltaX = ROOT.TCanvas("c_DeltaDeltaX", "c_DeltaDeltaX", 700, 700)
h_DeltaDeltaX.Draw("EP9")
h_DeltaDeltaX.Fit("gaus")
c_DeltaDeltaX.SaveAs("c_DeltaDeltaX.png")

c_AvgDeltaY = ROOT.TCanvas("c_AvgDeltaY", "c_AvgDeltaY", 700, 700)
h_AvgDeltaY.Draw("EP9")
h_AvgDeltaY.Fit("gaus")
c_AvgDeltaY.SaveAs("c_AvgDeltaY.png")


print("Angular Opening Delta(Delta(x)) between Thermal mockup and Piece of Glass: Mean = "
      + strIntRound(statistics.mean(v_DeltaDeltaX)*1000.) +
      " um, StdDev = "+strIntRound(statistics.stdev(v_DeltaDeltaX)*1000.) +
      " um")
print("Slide Avg(#delta(y)) between Thermal mockup and Piece of Glass = "
      + strIntRound(statistics.mean(v_AvgDeltaY)*1000.) +
      " um, StdDev = "+strIntRound(statistics.stdev(v_AvgDeltaY)*1000.) +
      " um")
print
