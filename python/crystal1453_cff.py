import FWCore.ParameterSet.Config as cms
                                        
common_beam_direction_parameters = cms.PSet(
    MinEta = cms.untracked.double(1.26821),
    MaxEta = cms.untracked.double(1.26821),
    MinPhi = cms.untracked.double(-0.040783 ),
    MaxPhi = cms.untracked.double(-0.040783 ),
    BeamMeanX = cms.untracked.double(0.0),
    BeamMeanY = cms.untracked.double(0.0),
    BeamPosition = cms.untracked.double(-26733.5)
)
