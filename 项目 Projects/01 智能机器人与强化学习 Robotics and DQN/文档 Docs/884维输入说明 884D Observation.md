# 884-dimensional historical observation

The historical course condition used four stacked observations. Each observation contained 180 LiDAR values and 41 engineered features, so the final input dimension was `4 x (180 + 41) = 884`.

This representation belongs to the historical Double Dueling DQN course experiment. It is not the representation used for the later algorithm-structure ablation, which fixed raw_4frame at 720 dimensions.

The later feature diagnostics found that the 41-feature implementation was structurally consistent and numerically finite. They also found a constant `global_max` feature and substantial correlation among feature pairs. Those diagnostics motivate the controlled comparison; they do not prove that engineered features are never useful.
