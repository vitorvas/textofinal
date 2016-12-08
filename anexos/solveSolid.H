{
    for (int nonOrth=0; nonOrth<=nNonOrthCorr; nonOrth++)
    {
        fvScalarMatrix hEqn
        (
           - fvm::laplacian(betav*alpha, h, "laplacian(alpha,h)")
           - Q
//           + fvOptions(rho, h)
//          Retorna um tmp<fvMatrix<type> > depois de fazer operações
//          na matriz do campo e na matriz criada internamente.
//          implementado em fvOptionListTemplates.C
        );

        hEqn.relax();
        hEqn.solve();
    }
}

thermo.correct();

Info<< "Min/max T:" << min(thermo.T()) << ' ' << max(thermo.T()) << endl;

