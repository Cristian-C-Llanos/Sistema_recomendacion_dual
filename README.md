# Sistema_recomendacion_dual
Sistema de recomendacion de video juegos y recetas culinarias
Modelo de recomendación dual
Universidad de caldas
Facultad de ingenierías
Autores
José Alexis Mejía
Cristian Camilo Llanos
 
1. Modelo propuesto
Existen diferentes tipos de sistemas de recomendación con propósitos variados que funcionan a partir de diferentes modelos, insumos y entornos, con este amplio espectro de opciones para este proyecto el modelo propuesto se basa en la utilización de APIs de sitios web especializados en la consolidación, puntuación y ranking de videojuegos y recetas culinarias. Este modelo de recomendación consta de dos etapas distintas: una primera fase donde se muestran por defecto los top de recetas o videojuegos basados en sus calificaciones, y una segunda fase donde se personaliza la recomendación de acuerdo con las preferencias del usuario

1.1 Perspectiva del modelo propuesto
En la primera etapa, el modelo accede a las APIs para mostrar por defecto los top de recetas o videojuegos basados en sus calificaciones y rankings actuales. Esta información inicial proporciona una visión general de las opciones más populares y mejor valoradas en cada categoría.
En la segunda etapa, el modelo permite la interacción del usuario para refinar las recomendaciones. En el caso de las recetas, se habilita la búsqueda por ingrediente, donde el usuario puede ingresar un ingrediente específico y el modelo devuelve el top de recetas que incluyen dicho ingrediente, junto con los detalles de la receta y los pasos de preparación. Para los videojuegos, además de mostrar los top de juegos con mejor calificación, se ofrece la posibilidad de ingresar la categoría de preferencia del usuario para obtener recomendaciones específicas en esa área.
Las entradas del modelo se basan en la información recopilada de las APIs, que incluyen datos de calificaciones, rankings y características de los videojuegos y recetas. Los procesos de recomendación se encargan de procesar esta información y generar recomendaciones personalizadas y relevantes para cada usuario.

1.2 Componentes del modelo
1.2.2 Componente 1: Entradas
Las entradas del modelo de recomendación de videojuegos y recetas culinarias se basan en la información recopilada de las APIs de sitios web especializados en la consolidación, puntuación y ranking de estos elementos. Para los videojuegos, se consideran datos como las calificaciones, géneros, plataformas y popularidad de cada juego. En cuanto a las recetas culinarias, se recopilan datos sobre los ingredientes, tipos de cocina, dificultad de preparación y valoraciones de los usuarios.
Además, se incluye la interacción del usuario como parte de las entradas, donde se permite ingresar preferencias específicas, como ingredientes para las recetas o categorías de videojuegos de interés. Estos datos proporcionados por el usuario se utilizan para personalizar las recomendaciones y ajustarlas a sus gustos individuales.

1.2.3 Componente 2: Proceso de Recomendación
El proceso de recomendación se encarga de analizar y procesar la información recopilada en las entradas para generar recomendaciones personalizadas y relevantes para los usuarios. En esta etapa, se utilizan algoritmos y técnicas de recomendación para identificar patrones, similitudes y preferencias de los usuarios.
Para los videojuegos, se aplican algoritmos de filtrado colaborativo y basados en contenido para recomendar juegos similares a los que el usuario ha disfrutado en el pasado, así como también se consideran las preferencias de género y plataforma. En el caso de las recetas, se emplean técnicas de filtrado basado en contenido para sugerir recetas que incluyan los ingredientes preferidos por el usuario.

1.2.3 Componente 3: Salidas
Las salidas del modelo de recomendación son las recomendaciones finales de videojuegos y recetas culinarias basados en puntaciones más altas. Estas recomendaciones se presentan de manera clara y detallada, al incluir información relevante como el nombre del juego o receta, calificaciones, ingredientes (en el caso de las recetas) y pasos de preparación. Además, se busca que las salidas sean adecuadas y satisfactorias para los usuarios, al brindar opciones que se ajusten a sus preferencias y gustos individuales. 

2. Estrategias de Aplicación del Modelo Propuesto
El modelo propuesto para el proyecto de recomendación de videojuegos y recetas culinarias se implementa a través de dos estrategias principales:
2.1 Estrategia de Selección
En esta estrategia, se enfoca en la adaptación guiada de los diferentes componentes del modelo para ofrecer recomendaciones personalizadas a los usuarios. Los pasos clave de esta estrategia son:
2.1.1 Identificación de Características de Usuario y de Ítem: Se analiza la información recopilada de las APIs, incluye calificaciones, rankings y características de videojuegos y recetas, para comprender las preferencias de los usuarios y las propiedades de los elementos recomendados.
2.1.2 Selección de Técnicas de Recomendación: Se eligen las técnicas de recomendación más adecuadas en función de la información disponible, en este caso se implementaron las técnicas Popularity-Based Recommendation y Content-Based Filtering.
2.1.3 Proceso de Recomendación Personalizada: Se ejecuta el proceso de recomendación para generar recomendaciones relevantes basada en popularidad (Popularity-Based Recommendation), este método recomienda los ítems más populares o mejor calificados a todos los usuarios, sin personalización, y recomendaciones adaptadas a las preferencias de cada usuario, al brindar una experiencia de búsqueda más enfocada y satisfactoria al utilizar el filtrado basado en contenido (Content-Based Filtering), este método recomienda ítems (juegos o recetas) basados en la similitud entre los atributos de los ítems y los atributos del usuario o sus preferencias explícitas.

2.2 Conclusiones del Capítulo
En conclusión, el modelo propuesto para la recomendación de videojuegos y recetas culinarias se basa en la utilización de APIs especializadas para acceder a información actualizada y relevante. Mediante dos etapas distintas, el modelo ofrece recomendaciones iniciales basadas en rankings y calificaciones, y luego permite la interacción del usuario para refinar las recomendaciones según sus preferencias específicas.
Las estrategias de selección permiten adaptar el modelo a las necesidades de los usuarios, al ofrecer recomendaciones personalizadas y relevantes en función de la información recopilada. En conjunto, este enfoque dinámico y adaptativo busca mejorar la experiencia de los usuarios al descubrir nuevos videojuegos y recetas culinarias que se ajusten a sus gustos y requerimientos individuales.
