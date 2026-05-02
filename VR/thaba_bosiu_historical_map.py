import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, Polygon, FancyBboxPatch
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.font_manager as fm

# Set up the figure with professional styling
plt.style.use('default')
fig, ax = plt.subplots(1, 1, figsize=(16, 12), dpi=300)

# Define colors for historical map aesthetic
colors = {
    'plateau': '#D2B48C',  # Tan for sandstone plateau
    'cliffs': '#8B7355',   # Dark brown for cliffs
    'roads': '#654321',    # Brown for roads
    'buildings': '#8B4513', # Saddle brown for buildings
    'water': '#4682B4',    # Steel blue for water springs
    'cultural_village': '#DEB887',  # Burlywood for cultural village
    'vegetation': '#228B22', # Forest green for vegetation
    'landmarks': '#B8860B', # Dark goldenrod for landmarks
    'text_bg': '#F5F5DC'   # Beige for text background
}

# Create the main Thaba Bosiu plateau (flat-topped mountain)
plateau_coords = [
    (3, 4), (13, 4), (14, 5), (14, 11), (13, 12), (3, 12), (2, 11), (2, 5)
]
plateau = Polygon(plateau_coords, closed=True, facecolor=colors['plateau'], 
                 edgecolor=colors['cliffs'], linewidth=3, alpha=0.8)
ax.add_patch(plateau)

# Add cliff indicators around the plateau
cliff_positions = [(2.5, 4.5), (13.5, 4.5), (13.5, 11.5), (2.5, 11.5)]
for pos in cliff_positions:
    cliff = Rectangle(pos, 0.5, 7, facecolor=colors['cliffs'], alpha=0.6)
    ax.add_patch(cliff)

# Add the six historical passes with labels
passes = {
    'Khubelu Pass': [(2, 8), (1, 8)],
    'Ramaseli Pass': [(2, 6), (1, 6)],
    'Maebeng Pass': [(8, 4), (8, 3)],
    'Mokachane Pass': [(10, 4), (10, 3)],
    'Makara Pass': [(13, 7), (14, 7)],
    'Rahebe Pass': [(13, 9), (14, 9)]
}

for pass_name, coords in passes.items():
    ax.plot([coords[0][0], coords[1][0]], [coords[0][1], coords[1][1]], 
            color=colors['roads'], linewidth=2, linestyle='--', alpha=0.7)
    ax.text(coords[1][0]-0.5, coords[1][1]+0.3, pass_name, 
            fontsize=8, ha='right', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=colors['text_bg'], alpha=0.8))

# Add eight water springs on the plateau
springs = [
    (4, 10), (6, 9), (8, 10), (10, 9),
    (5, 7), (7, 6), (9, 7), (11, 8)
]
for i, spring in enumerate(springs):
    spring_circle = Circle(spring, 0.2, facecolor=colors['water'], 
                          edgecolor='navy', linewidth=1, alpha=0.8)
    ax.add_patch(spring_circle)
    ax.text(spring[0], spring[1]-0.5, f'Spring {i+1}', 
            fontsize=7, ha='center', style='italic')

# Add Moshoeshoe I's stone buildings (historical compound)
moshoeshoe_buildings = [
    {'pos': (6, 11), 'size': (1, 0.5), 'label': "Moshoeshoe's House"},
    {'pos': (8, 11), 'size': (0.8, 0.5), 'label': 'Building 2'},
    {'pos': (10, 11), 'size': (0.8, 0.5), 'label': 'Building 3'},
    {'pos': (4, 9), 'size': (0.8, 0.5), 'label': 'Building 4'},
    {'pos': (12, 9), 'size': (0.5, 0.5), 'label': 'Cylindrical Building'}
]

for building in moshoeshoe_buildings:
    rect = Rectangle(building['pos'], building['size'][0], building['size'][1],
                   facecolor=colors['buildings'], edgecolor='black', 
                   linewidth=1, alpha=0.8)
    ax.add_patch(rect)
    ax.text(building['pos'][0] + building['size'][0]/2, building['pos'][1] - 0.3,
            building['label'], fontsize=7, ha='center', fontweight='bold')

# Add Thaba Bosiu Cultural Village (at the base of the mountain)
cultural_village = FancyBboxPatch((0.5, 0.5), 4, 2.5, 
                                 boxstyle="round,pad=0.1",
                                 facecolor=colors['cultural_village'], 
                                 edgecolor=colors['landmarks'], 
                                 linewidth=2, alpha=0.7)
ax.add_patch(cultural_village)

# Add Cultural Village facilities
cv_features = [
    {'pos': (1, 2.5), 'label': 'Visitor Centre'},
    {'pos': (2, 2.5), 'label': 'Museum'},
    {'pos': (3, 2.5), 'label': 'Restaurant'},
    {'pos': (1, 1.5), 'label': 'Traditional Homesteads'},
    {'pos': (3, 1.5), 'label': 'Hotel'},
    {'pos': (2, 1), 'label': 'Cultural Displays'}
]

for feature in cv_features:
    ax.text(feature['pos'][0], feature['pos'][1], feature['label'],
            fontsize=8, ha='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

# Add Mount Qiloane (distinctive conical landmark)
qiloane = patches.RegularPolygon((15, 8), 3, radius=1.2, 
                                facecolor=colors['vegetation'], 
                                edgecolor='darkgreen', linewidth=2, alpha=0.7)
ax.add_patch(qiloane)
ax.text(15, 6.5, 'Mount Qiloane\n(Inspiration for\nBasotho Hat)', 
        fontsize=9, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=colors['text_bg'], alpha=0.8))

# Add main access roads
main_roads = [
    {'start': (8, 0), 'end': (8, 3), 'label': 'Access Road from Maseru'},
    {'start': (0, 1.75), 'end': (16, 1.75), 'label': 'A2 Main Road'},
    {'start': (14, 7), 'end': (16, 7), 'label': 'Local Road'}
]

for road in main_roads:
    ax.plot([road['start'][0], road['end'][0]], [road['start'][1], road['end'][1]],
            color=colors['roads'], linewidth=3, alpha=0.8)
    mid_x = (road['start'][0] + road['end'][0]) / 2
    mid_y = (road['start'][1] + road['end'][1]) / 2
    ax.text(mid_x, mid_y + 0.3, road['label'], fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9))

# Add San rock art site
rock_art = Circle((11, 6), 0.3, facecolor='orange', edgecolor='red', 
                 linewidth=2, alpha=0.7)
ax.add_patch(rock_art)
ax.text(11, 5.4, 'San Rock Art Site', fontsize=8, ha='center', fontweight='bold')

# Add historical battle sites
battle_sites = [
    {'pos': (1, 8), 'label': 'Mzilikazi Attack Site (1826)'},
    {'pos': (14, 10), 'label': 'Boer Siege Position (1865)'},
    {'pos': (2, 7), 'label': "Wepener's Fall Site"}
]

for site in battle_sites:
    ax.plot(site['pos'][0], site['pos'][1], 'r^', markersize=10, alpha=0.8)
    ax.text(site['pos'][0], site['pos'][1] - 0.5, site['label'],
            fontsize=8, ha='center', color='darkred', fontweight='bold')

# Set up the map
ax.set_xlim(-1, 17)
ax.set_ylim(0, 13)
ax.set_aspect('equal')

# Add title and subtitle
ax.text(8, 12.5, 'HISTORICAL MAP OF THABA BOSIU & THABA BOSIU CULTURAL VILLAGE',
        fontsize=16, ha='center', fontweight='bold', color='darkblue')
ax.text(8, 12, 'Lesotho - Mountain Fortress of Moshoeshoe I (1824-1868)',
        fontsize=12, ha='center', style='italic', color='darkblue')

# Add scale bar
scale_bar = Line2D([12, 14], [0.5, 0.5], linewidth=3, color='black')
ax.add_line(scale_bar)
ax.text(13, 0.2, '1 km', fontsize=10, ha='center', fontweight='bold')
ax.text(13, 0.8, 'Scale', fontsize=9, ha='center', style='italic')

# Add compass rose
compass_x, compass_y = 15.5, 11.5
ax.plot(compass_x, compass_y + 0.5, compass_x, compass_y - 0.5, 'k-', linewidth=2)
ax.plot(compass_x - 0.5, compass_y, compass_x + 0.5, compass_y, 'k-', linewidth=2)
ax.text(compass_x, compass_y + 0.7, 'N', fontsize=12, ha='center', fontweight='bold')
ax.text(compass_x + 0.7, compass_y, 'E', fontsize=10, ha='center')
ax.text(compass_x, compass_y - 0.7, 'S', fontsize=10, ha='center')
ax.text(compass_x - 0.7, compass_y, 'W', fontsize=10, ha='center')

# Create legend
legend_elements = [
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=colors['plateau'],
               markersize=10, label='Thaba Bosiu Plateau'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['water'],
               markersize=8, label='Natural Springs'),
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=colors['buildings'],
               markersize=8, label='Historical Buildings'),
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=colors['cultural_village'],
               markersize=10, label='Cultural Village'),
    plt.Line2D([0], [0], color=colors['roads'], linewidth=3, label='Roads'),
    plt.Line2D([0], [0], marker='^', color='w', markerfacecolor='red',
               markersize=8, label='Battle Sites'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='orange',
               markersize=8, label='Rock Art Site')
]

ax.legend(handles=legend_elements, loc='upper left', fontsize=9,
         framealpha=0.9, fancybox=True, shadow=True)

# Add grid for reference
ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)

# Remove axis labels for cleaner look
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Add information box
info_text = (
    "Key Historical Facts:\n"
    "• Established 1824 by Moshoeshoe I\n"
    "• Capital of Basotho nation\n"
    "• 8 natural springs, 6 passes\n"
    "• Never conquered in battle\n"
    "• National Monument since 1967"
)
ax.text(0.5, 11.5, info_text, fontsize=9, 
        bbox=dict(boxstyle='round,pad=0.5', facecolor=colors['text_bg'], 
                 edgecolor='darkblue', linewidth=2, alpha=0.9),
        verticalalignment='top')

plt.tight_layout()
plt.savefig('c:\\Users\\iiii\\Desktop\\VR\\Thaba_Bosiu_Historical_Map.png', 
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print("Historical map of Thaba Bosiu and Cultural Village created successfully!")
print("Map saved as: Thaba_Bosiu_Historical_Map.png")
