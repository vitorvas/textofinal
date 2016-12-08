    solidThermo& thermo = thermos[i];

    tmp<volScalarField> trho = thermo.rho();

    tmp<volScalarField> tcp = thermo.Cp();

    tmp<volScalarField> talpha = thermo.alpha();
    const volScalarField& alpha = talpha();
    tmp<volScalarField> tkappa = thermo.kappa();

    volScalarField& h = thermo.he();

    const volScalarField& betav = betavSolid[i];

    // OpenFoam's original IOoptionsList introduced in version 2.2.2 is removed
    // fv::IOoptionList& fvOptions = solidHeatSources[i];

    // Added to use my own source-term
    // When reading from another file, it should be done at
    // this point, before atributing the qVol to const Q field

    // 13/04/2015
    // ------------------------------------------------------------------
    // CHANGE from former implementation.
    // Q (former qvol) is only read as a default file in OpenFOAM format.
    // if it is not present, Q is assumed 0 in the first step.
    // ------------------------------------------------------------------

    // First of all, only do that if the solid is the fuel
if (solidRegions[i].name() == "fuel")
  {
    // Create a scalar field from the values read from Q file in
    // solids directories
    scalarField sF = scalarField(qVol[i].internalField());
    scalarField completeSF(qVol[i].internalField().size()*Pstream::nProcs(), 0.0);
    
    // Values in qVol[i] are dimensioned values.
    // Pay attention on this before assigning it to the vector.
    
    // This is only necessary if running in parallel
    if(Pstream::parRun())
      {
	fileName cellCorr(runTime.rootPath()+"/"+runTime.caseName()+
			  "/constant/fuel/polyMesh");

	// Read cellProcAddressing for each processor
	labelIOList procList
	  (
	   IOobject
	   (
	    "cellProcAddressing", 			   		// Name
	    cellCorr,
	    mesh,  			// Registry
	    IOobject::MUST_READ, 	// Read option
	    IOobject::NO_WRITE 		// Write Option
	    ),
	   procList
	   );

	procLabelList[Pstream::myProcNo()] = procList;

	Pout << " --- ADDED: procLabelList[" << Pstream::myProcNo()
	     << "]: " << procList;
	
	Pstream::gatherList<scalarField>(procScalarFieldList);
	Pstream::scatterList<scalarField>(procScalarFieldList);
	
	Pout << " --- ADDED: procList: " << procList << endl;
	
      }

// If the file is not present, use current qVol[i] (the volScalarField)
const volScalarField& Q = qVol[i];


 
