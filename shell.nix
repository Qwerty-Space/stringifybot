{ pkgs ? import <nixpkgs> {} }:
let
  bprint = { lib, buildPythonPackage, fetchFromGitHub }:
    buildPythonPackage rec {
      pname = "beauty-print";
      version = "0.6.1";

      src = fetchFromGitHub {
        owner = "udf";
        repo = "bprint";
        rev = "4e36f0687bbea1ca3cd5430c8f461792300e3086";
        sha256 = "0hjlh53lzslv3c6nzd087s9ylvaja0k48ij391j9c7a95s785zvj";
      };

      doCheck = false;
    };
in
pkgs.mkShell {
  name = "stringify-bot-shell";
  buildInputs = [
    (pkgs.python39.withPackages (ps: with ps; [
      (callPackage bprint {})
      (callPackage ./telethon.nix {})
    ]))
  ];
}