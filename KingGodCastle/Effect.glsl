//_______Version 0.9 _______
---VERTEX SHADER---
$HEADER$

varying vec2 v_tex_coord;

void main() {
    
    v_tex_coord = vTexCoords0;
    
    gl_Position = projection_mat * modelview_mat * vec4(vPosition, 0.0, 1.0);

}

---FRAGMENT SHADER---
$HEADER$


// Fragment shader code here
varying vec2 v_tex_coord;

uniform float time;
uniform float strength;
uniform vec3 colour;
uniform float speedmodifier;

void main() {      


    float val = smoothstep(0.1,1.0,time*speedmodifier);
    vec3 red = vec3(
    1.0 * val * v_tex_coord.y,
    0.0 * val * v_tex_coord.y,
    0.0 * val * v_tex_coord.y
    );
    
   
   vec3 rescolor = colour * val * v_tex_coord.y;
    
    //gl_FragColor = vec4(vec3(red), 1.0);
    gl_FragColor = vec4(rescolor,strength);
    
}

