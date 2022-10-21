from script.PARXER                                          import numerical_value
from script.PARXER.PRINT                                    import show_data
from script.LEXER.FUNCTION                                  import print_value
from statement                                              import mainStatement as MS
from script.PARXER.PARXER_FUNCTIONS._UNLESS_                import unless_statement
from script.PARXER.PARXER_FUNCTIONS._IF_                    import if_statement
from script.PARXER.PARXER_FUNCTIONS._SWITCH_                import switch_statement
from script.PARXER.PARXER_FUNCTIONS.WHILE                   import while_statement
from script.PARXER.PARXER_FUNCTIONS._FOR_                   import end_for_else
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_         import comment as cmt
from script.PARXER.PARXER_FUNCTIONS._TRY_                   import try_statement
from script.PARXER.PARXER_FUNCTIONS._FOR_                   import for_try
from script.PARXER.PARXER_FUNCTIONS._FOR_.IF.WINDOWS        import WindowsIF as wIF
from script.PARXER.PARXER_FUNCTIONS._FOR_.UNLESS            import WindowsUnless as wU
from script.PARXER.PARXER_FUNCTIONS._FOR_.SWITCH.WINDOWS    import WindowsSwitch as WSw
from script.PARXER.PARXER_FUNCTIONS._FOR_                   import for_block_treatment
from script.PARXER                                          import module_load_treatment 
from script.STDIN.LinuxSTDIN                                import bm_configure as bm
from src.modulesLoading                                     import modules, moduleMain 
from script.PARXER.PARXER_FUNCTIONS._FOR_.WHILE.WINDOWS     import WindowsWhile as WWh
from script.PARXER.PARXER_FUNCTIONS._FOR_.BEGIN.WINDOWS     import begin
from src.functions.windows                                  import windowsDef as WD
from src.classes.windows                                    import windowsClass as WC
from script.PARXER                                          import partial_assembly