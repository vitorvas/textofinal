    // Solve the Momentum equation
    tmp<fvVectorMatrix> UEqn
    (
        fvm::div(phi, U)
      + turb.divDevRhoReff(U)
     ==
        fvOptions(rho, U)
    );

    UEqn().relax();

    fvOptions.constrain(UEqn());

    solve
    (
        UEqn()
     ==
        fvc::reconstruct
        (
            (
              - ghf*fvc::snGrad(rho)
              - fvc::snGrad(p_rgh)
            )*mesh.magSf()

	    // Important:
	    // ghf*fvc::snGrad(rho) comes from pressure adjustment.
	    // p_rgh is p adjusted by density.
	    // When the gradient is calculated for p_rgh the spurious
	    // non-physical term which arises is compensated by
	    // subtracting p_rgh
        )
    );

    fvOptions.correct(U);
